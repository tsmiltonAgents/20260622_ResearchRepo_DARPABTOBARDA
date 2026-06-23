"""Helpers for the autonomous loop: normalize amounts + funder_type, append rows to the CSVs."""
import csv, re, os

FX = {'$':1.0,'US$':1.0,'USD':1.0,'£':1.27,'GBP':1.27,'€':1.08,'EUR':1.08,'DKK':0.145}
_NUM = r'[\d][\d,]*(?:\.\d+)?'
_TOKEN = re.compile(r'(?P<cur>USD|GBP|EUR|DKK|US\$|\$|£|€)?\s*(?P<num>'+_NUM+r')\s*(?P<suf>billion|million|bn|b|m|k)?(?![A-Za-z])', re.I)

def parse_amount(s):
    s=(s or '').strip(); low=s.lower()
    if not s: return ''
    if any(w in low for w in ['undisclosed','not disclosed','no public','unknown','not public','undisc','n/a','no dollar','not found','tbd','redacted','not itemized','not separately']):
        return ''
    has_usd = bool(re.search(r'(?:US\$|\$|USD)\s*'+_NUM, s, re.I))
    vals=[]
    for mt in _TOKEN.finditer(s):
        cur,num,suf=mt.group('cur'),mt.group('num'),mt.group('suf')
        if num is None: continue
        if cur is None and not suf: continue
        if has_usd and cur not in ('$','US$','USD',None): continue
        cur2={'us$':'$'}.get((cur or '$').lower(), cur or '$'); rate=FX.get(cur2,FX.get(cur2.upper(),1.0))
        val=float(num.replace(',','')); sf=(suf or '').lower()
        if sf in ('billion','bn','b'): m=val*1000
        elif sf in ('million','m'): m=val
        elif sf=='k': m=val/1000.0
        else: m = val/1e6 if val>=1000 else val
        vals.append(m*rate)
    if not vals: return ''
    agg=max(vals)
    return str(round(agg,3)) if agg<10 else str(round(agg,1))

_HHS={'NIH/NIAID','NIH','CDC','ASPR','BARDA','ARPA-H','BARDA/ASPR','CDC/EPA','NIOSH/NPPTL'}
_DOD={'DTRA','JPEO-CBRND','USAMRIID/DoD','DARPA BTO','DLA/HHS'}
_IC={'IARPA','In-Q-Tel'}
_USGOV={'DHS','USAID','USDA','State Dept','DOE/NNSA','NSF','EPA'}
_MULTI={'CEPI','Trinity Challenge','Global Fund','IAVI','Gavi','WHO','Unitaid','FIND','DNDi','GARDP','Pandemic Fund','World Bank'}
def ftype(f, default='foundation/philanthropy'):
    if f in _HHS: return 'US HHS'
    if f in _DOD: return 'US DoD'
    if f in _IC: return 'US IC'
    if f in _USGOV: return 'US gov agency'
    if f in _MULTI: return 'multilateral/nonprofit'
    return default

ROOT=os.path.join(os.path.dirname(__file__),'..','data')
def append_programs(rows):
    # rows: list of dict with funder,program,acronym_expansion,theme,pandemic_relevance,years,status,source_file,[funder_type]
    path=os.path.join(ROOT,'programs.csv'); hdr=list(csv.reader(open(path)))[0]
    with open(path,'a',newline='') as f:
        w=csv.writer(f)
        for r in rows:
            r.setdefault('funder_type', ftype(r['funder'], r.get('_default','foundation/philanthropy')))
            w.writerow([r.get(c,'') for c in hdr])
def append_awards(rows):
    # rows: list of dict with funder,program,recipient,amount,year,theme,purpose,source_file,[funder_type],[amount_basis]
    path=os.path.join(ROOT,'awards.csv'); hdr=list(csv.reader(open(path)))[0]
    with open(path,'a',newline='') as f:
        w=csv.writer(f)
        for r in rows:
            r.setdefault('funder_type', ftype(r['funder'], r.get('_default','foundation/philanthropy')))
            r.setdefault('amount_usd_millions', parse_amount(r.get('amount','')))
            r.setdefault('amount_basis','')
            w.writerow([r.get(c,'') for c in hdr])
