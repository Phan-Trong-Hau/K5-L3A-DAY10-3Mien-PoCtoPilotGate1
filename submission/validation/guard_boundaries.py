import copy,json,sys
from pathlib import Path
from types import SimpleNamespace
sys.path.insert(0,str(Path.cwd()))
from lab10.guards import write_gate
from lab10.world import World
from lab10.tools import ReadTools
base=json.loads(Path('data/world.json').read_text())
count=0
def fixture():
 w=World(base);tools=ReadTools(w);ticket={'ticket_id':'NEW-CLAIM','order_id':'O-1001','customer_id':'C-01'}
 ctx=SimpleNamespace(ticket=ticket,tools=tools,as_of=w.as_of,gates={'business':{'daily_refund_cap_vnd':2000000},'operations':{'approver_id':'NV-HANH'}})
 action={'tool':'issue_refund','ticket_id':ticket['ticket_id'],'order_id':ticket['order_id'],'amount_vnd':25000,'payer':'LOGIX','basis':'policy','approval_id':None}
 return w,ctx,action

def check(name,mutate,expected):
 global count
 w,c,a=fixture();mutate(w,c,a);before=copy.deepcopy((w.ledger,w.faults));result=write_gate(c,a);assert result.action==expected,(name,result);assert before==(w.ledger,w.faults),name;count+=1

def approval(w,c,a):
 a['approval_id']='NEW-APPROVAL';w.data['approvals'].append({'approval_id':a['approval_id'],'ticket_id':c.ticket['ticket_id'],'order_id':a['order_id'],'customer_id':c.ticket['customer_id'],'approver_id':'NV-HANH','expires_at':c.as_of,'status':'valid','max_vnd':25000})
check('normal auto refund',lambda w,c,a:None,'allow')
check('valid approval inclusive expiry',approval,'allow')
for field,value in [('ticket_id','OTHER'),('order_id','OTHER'),('customer_id','OTHER'),('approver_id','OTHER'),('status','used'),('status','revoked'),('expires_at','2020-01-01'),('expires_at','invalid'),('max_vnd',24999),('max_vnd',True),('max_vnd',float('nan')),('max_vnd',float('inf'))]:
 def mutate(w,c,a,field=field,value=value):approval(w,c,a);w.data['approvals'][-1][field]=value
 check('invalid '+field+' '+str(value),mutate,'escalate')
check('unknown approval',lambda w,c,a:a.update(approval_id='MISSING'),'escalate')
def used(w,c,a,amount,cap=50000):
 approval(w,c,a);w.data['approvals'][-1]['max_vnd']=cap;w.ledger.append({'approval_id':a['approval_id'],'amount_vnd':amount,'order_id':'OTHER','customer_id':'C-01'})
check('approval remaining exactly sufficient',lambda w,c,a:used(w,c,a,25000),'allow')
check('approval remaining insufficient',lambda w,c,a:used(w,c,a,25001),'escalate')
def spent(w,c,a,total):
 # Existing undated rows are counted conservatively, including seed rows.
 existing=sum(r['amount_vnd'] for r in w.ledger if r['customer_id']=='C-01' and not r.get('approval_id'))
 w.ledger.append({'amount_vnd':total-existing,'order_id':'OTHER','customer_id':'C-01','approval_id':None})
check('customer exactly at cap',lambda w,c,a:spent(w,c,a,275000),'allow')
check('customer cap exceeded',lambda w,c,a:spent(w,c,a,275001),'escalate')
def approved_over_customer_cap(w,c,a):spent(w,c,a,300000);approval(w,c,a)
check('valid human approval above customer automatic cap',approved_over_customer_cap,'allow')
def strikes(w,c,a,n):
 o=c.tools.lookup_order(a['order_id']);w.faults=[{'carrier_id':o['parcels'][0]['carrier_id']} for _ in range(n)]
check('second carrier strike allowed',lambda w,c,a:strikes(w,c,a,1),'allow')
check('third carrier strike escalates before refund',lambda w,c,a:strikes(w,c,a,2),'escalate')
def direct_fault(w,c,a):
 strikes(w,c,a,2);p=c.tools.lookup_order(a['order_id'])['parcels'][0];a.update(tool='file_carrier_fault',parcel_id=p['parcel_id'],carrier_id=p['carrier_id'],driver_id=p.get('driver_id'),delay_days=4)
check('direct third carrier strike blocked',direct_fault,'escalate')
def over_auto(w,c,a):
 for p in w.data['policies']:p['auto_limit_vnd']=10000
check('approval required above policy auto limit',over_auto,'escalate')
print(f'{count} boundary/security checks passed; guard calls caused no ledger/fault side effects.')
