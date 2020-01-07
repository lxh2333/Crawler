import re

from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from message.models import *
from pyecharts import Bar
list_jd = []
list_taobao = []
list_sge=[]
list_avg_sge=[]
list_var_sge=[]
def lshq_sge(request):
    sum_Au95 = 0
    sum_Au99 = 0
    sum_Au100 = 0
    sum_iAu99 = 0
    sum_AuTD = 0
    sum_AuTN1 = 0
    sum_AuTN2 = 0
    sum_mAuTD = 0
    sum_Pt95 = 0
    sum_Ag99 = 0
    sum_AgTD = 0
    sum_PGC = 0
    sum_Au95_var =0
    sum_Au99_var =0
    sum_Au100_var =0
    sum_iAu99_var =0
    sum_AuTD_var =0
    sum_AuTN1_var =0
    sum_AuTN2_var =0
    sum_mAuTD_var =0
    sum_Pt95_var =0
    sum_Ag99_var =0
    sum_AgTD_var =0
    sum_PGC_var = 0
    jd = jdprice.objects.filter(source='jd')
    taobao = tbprice.objects.filter(source='taobao')
    sge=sgeprice.objects.filter(source='sge').order_by('-date')
    count_jd=len(jd)
    count_sge=len(sge)
    count_Ag99 = count_sge
    count_PGC = count_sge
    for i in range(len(sge)):
        Au95 = re.split('/', sge[i].Au95)
        Au95_start = Au95[0]
        Au95_end = Au95[1]
        Au95_change = Au95[2]
        Au95_rate = Au95[3]
        Au95_avg = Au95[4]
        Au99 = re.split('/', sge[i].Au99)
        Au99_start = Au99[0]
        Au99_end = Au99[1]
        Au99_change = Au99[2]
        Au99_rate = Au99[3]
        Au99_avg = Au99[4]
        Au100 = re.split('/', sge[i].Au100)
        Au100_start = Au100[0]
        Au100_end = Au100[1]
        Au100_change = Au100[2]
        Au100_rate = Au100[3]
        Au100_avg = Au100[4]
        iAu99 = re.split('/', sge[i].iAu99)
        iAu99_start = iAu99[0]
        iAu99_end = iAu99[1]
        iAu99_change = iAu99[2]
        iAu99_rate = iAu99[3]
        iAu99_avg = iAu99[4]
        AuTD = re.split('/', sge[i].AuTD)
        AuTD_start = AuTD[0]
        AuTD_end = AuTD[1]
        AuTD_change = AuTD[2]
        AuTD_rate = AuTD[3]
        AuTD_avg = AuTD[4]
        AuTN1 = re.split('/', sge[i].AuTN1)
        AuTN1_start = AuTN1[0]
        AuTN1_end = AuTN1[1]
        AuTN1_change = AuTN1[2]
        AuTN1_rate = AuTN1[3]
        AuTN1_avg = AuTN1[4]
        AuTN2 = re.split('/', sge[i].AuTN2)
        AuTN2_start = AuTN2[0]
        AuTN2_end = AuTN2[1]
        AuTN2_change = AuTN2[2]
        AuTN2_rate = AuTN2[3]
        AuTN2_avg = AuTN2[4]
        mAuTD = re.split('/', sge[i].mAuTD)
        mAuTD_start = mAuTD[0]
        mAuTD_end = mAuTD[1]
        mAuTD_change = mAuTD[2]
        mAuTD_rate = mAuTD[3]
        mAuTD_avg = mAuTD[4]
        Pt95 = re.split('/', sge[i].Pt95)
        Pt95_start = Pt95[0]
        Pt95_end = Pt95[1]
        Pt95_change = Pt95[2]
        Pt95_rate = Pt95[3]
        Pt95_avg = Pt95[4]
        if not sge[i].Ag99 == '-':
            Ag99 = re.split('/', sge[i].Ag99)
            Ag99_start = Ag99[0]
            Ag99_end = Ag99[1]
            Ag99_change = Ag99[2]
            Ag99_rate = Ag99[3]
            Ag99_avg = Ag99[4]
        else:
            Ag99_start = "-"
            Ag99_end = "-"
            Ag99_change = "-"
            Ag99_rate = "-"
            Ag99_avg = "-"
        AgTD = re.split('/', sge[i].AgTD)
        AgTD_start = AgTD[0]
        AgTD_end = AgTD[1]
        AgTD_change = AgTD[2]
        AgTD_rate = AgTD[3]
        AgTD_avg = AgTD[4]
        if not sge[i].PGC =='-':
            PGC = re.split('/', sge[i].PGC)
            PGC_start = PGC[0]
            PGC_end = PGC[1]
            PGC_change = PGC[2]
            PGC_rate = PGC[3]
            PGC_avg = PGC[4]
        else:
            PGC_start = "-"
            PGC_end = "-"
            PGC_change = "-"
            PGC_rate = "-"
            PGC_avg = "-"
        data_sge={'Au95_start':Au95_start,'Au99_start':Au99_start,'Au100_start':Au100_start,'iAu99_start':iAu99_start,
                  'AuTD_start':AuTD_start,'AuTN1_start':AuTN1_start,'AuTN2_start':AuTN2_start,'mAuTD_start':mAuTD_start,
                  'Pt95_start':Pt95_start,'Ag99_start':Ag99_start,'AgTD_start':AgTD_start,'PGC_start':PGC_start,
                  'Au95_end': Au95_end, 'Au99_end': Au99_end, 'Au100_end': Au100_end,
                  'iAu99_end': iAu99_end,
                  'AuTD_end': AuTD_end, 'AuTN1_end': AuTN1_end, 'AuTN2_end': AuTN2_end,
                  'mAuTD_end': mAuTD_end,
                  'Pt95_end': Pt95_end, 'Ag99_end': Ag99_end, 'AgTD_end': AgTD_end, 'PGC_end': PGC_end,
                  'Au95_change': Au95_change, 'Au99_change': Au99_change, 'Au100_change': Au100_change,
                  'iAu99_change': iAu99_change,
                  'AuTD_change': AuTD_change, 'AuTN1_change': AuTN1_change, 'AuTN2_change': AuTN2_change,
                  'mAuTD_change': mAuTD_change,
                  'Pt95_change': Pt95_change, 'Ag99_change': Ag99_change, 'AgTD_change': AgTD_change, 'PGC_change': PGC_change,
                  'Au95_rate': Au95_rate, 'Au99_rate': Au99_rate, 'Au100_rate': Au100_rate,
                  'iAu99_rate': iAu99_rate,
                  'AuTD_rate': AuTD_rate, 'AuTN1_rate': AuTN1_rate, 'AuTN2_rate': AuTN2_rate,
                  'mAuTD_rate': mAuTD_rate,
                  'Pt95_rate': Pt95_rate, 'Ag99_rate': Ag99_rate, 'AgTD_rate': AgTD_rate, 'PGC_rate': PGC_rate,
                  'Au95_avg': Au95_avg, 'Au99_avg': Au99_avg, 'Au100_avg': Au100_avg,
                  'iAu99_avg': iAu99_avg,
                  'AuTD_avg': AuTD_avg, 'AuTN1_avg': AuTN1_avg, 'AuTN2_avg': AuTN2_avg,
                  'mAuTD_avg': mAuTD_avg,
                  'Pt95_avg': Pt95_avg, 'Ag99_avg': Ag99_avg, 'AgTD_avg': AgTD_avg, 'PGC_avg': PGC_avg,
                  'date':sge[i].date}
        list_sge.append(data_sge)
        """
        sum_Au95 +=float(sge[i].Au95)
        sum_Au99 +=float(sge[i].Au99)
        sum_Au100 +=float(sge[i].Au100)
        sum_iAu99 +=float(sge[i].iAu99)
        sum_AuTD +=float(sge[i].AuTD)
        sum_AuTN1 +=float(sge[i].AuTN1)
        sum_AuTN2 +=float(sge[i].AuTN2)
        sum_mAuTD +=float(sge[i].mAuTD)
        sum_Pt95 +=float(sge[i].Pt95)
        if sge[i].Ag99 == '-':
            count_Ag99 = count_Ag99-1
        else:
            sum_Ag99 +=float(sge[i].Ag99)
        sum_AgTD +=float(sge[i].AgTD)
        if sge[i].PGC == '-':
            count_PGC = count_PGC-1
        else:
            sum_PGC +=float(sge[i].PGC)
        sum_Au95_var += float(sge[i].Au95)**2
        sum_Au99_var += float(sge[i].Au99)**2
        sum_Au100_var += float(sge[i].Au100)**2
        sum_iAu99_var += float(sge[i].iAu99)**2
        sum_AuTD_var += float(sge[i].AuTD)**2
        sum_AuTN1_var += float(sge[i].AuTN1)**2
        sum_AuTN2_var += float(sge[i].AuTN2)**2
        sum_mAuTD_var += float(sge[i].mAuTD)**2
        sum_Pt95_var += float(sge[i].Pt95)**2
        if not sge[i].Ag99 == '-':
            sum_Ag99_var += float(sge[i].Ag99)**2
        sum_AgTD_var += float(sge[i].AgTD)**2
        if not sge[i].PGC == '-':
            sum_PGC_var += float(sge[i].PGC)**2
    data_avg_sge = {'avg_Au95':Avg(sum_Au95,count_sge),'avg_Au99':Avg(sum_Au99,count_sge),'avg_Au100':Avg(sum_Au100,count_sge),
                    'avg_iAu99':Avg(sum_iAu99,count_sge),'avg_AuTD':Avg(sum_AuTD,count_sge),'avg_AuTN1':Avg(sum_AuTN1,count_sge),
                    'avg_AuTN2':Avg(sum_AuTN2,count_sge),'avg_mAuTD':Avg(sum_mAuTD,count_sge),'avg_Pt95':Avg(sum_Pt95,count_sge),
                    'avg_Ag99':Avg(sum_Ag99,count_Ag99),'avg_AgTD':Avg(sum_AgTD,count_sge),'avg_PGC':Avg(sum_PGC,count_PGC)}
    list_avg_sge.append(data_avg_sge)
    data_var_sge = {'var_Au95':Var(sum_Au95_var,sum_Au95,count_sge),'var_Au99':Var(sum_Au99_var,sum_Au99,count_sge),
                    'var_Au100':Var(sum_Au100_var,sum_Au100,count_sge),'var_iAu99':Var(sum_iAu99_var,sum_iAu99,count_sge),
                    'var_AuTD':Var(sum_AuTD_var,sum_AuTD,count_sge),'var_AuTN1':Var(sum_AuTN1_var,sum_AuTN1,count_sge),
                    'var_AuTN2':Var(sum_AuTN2_var,sum_AuTN2,count_sge),'var_mAuTD':Var(sum_mAuTD_var,sum_mAuTD,count_sge),
                    'var_Pt95':Var(sum_Pt95_var,sum_Pt95,count_sge),'var_Ag99':Var(sum_Ag99_var,sum_Ag99,count_Ag99),
                    'var_AgTD':Var(sum_AgTD_var,sum_AgTD,count_sge),'var_PGC':Var(sum_PGC_var,sum_PGC,count_PGC)}
    list_var_sge.append(data_var_sge)
    """
    return render(request, 'lshq_sge.html', {'form_sge':list_sge})
def Avg(sum,count):
    avg = float(sum/count)
    return round(avg,2)
def Var(sum_var,sum,count):
    mean = sum/count
    var = (sum_var/count)-(mean**2)
    return round(var,2)
def lshq_ctf(request):
    list_jd_ctf = []
    jd = jdprice.objects.filter(shop__contains='周大福').order_by('-date')
    date = [line['date'] for line in jd]
    dates = list(set(date))
    date_now = 0
    for i in range(len(date)):
        if date[i] == dates[len(dates) - 1]:
            date_now += 1
    for i in range(date_now):
        history_jd = []
        jd_url = jdprice.objects.filter(url=jd[i].url).order_by('-date')
        for j in range(len(jd_url)):
            history = jd_url[j].price + '('+jd_url[j].date + ')'
            history_list = {'history':history}
            history_jd.append(history_list)
        data_jd_ctf = {'url':jd[i].url,'name':jd[i].name,'price':jd[i].price,'date':jd[i].date,"history":history_jd,'num':len(history_jd)}
        list_jd_ctf.append(data_jd_ctf)
    return render(request, 'lshq_ctf.html', {'form_ctf_jd':list_jd_ctf})
def lshq_ctf_tmall(request):
    list_tmall_ctf=[]
    tmall = tmallprice.objects.filter(shop__contains='周大福').order_by('-date')
    date = [line['date'] for line in tmall]
    dates = list(set(date))
    date_now = 0
    for i in range(len(date)):
        if date[i] == dates[len(dates) - 1]:
            date_now += 1
    for i in range(date_now):
        history_tmall = []
        url = re.split(r'=',tmall[i].url)
        id = re.split(r'&',url[1])[0]
        tmall_url = tmallprice.objects.filter(url__contains=id).order_by('-date')
        for j in range(len(tmall_url)):
            history = tmall_url[j].price + '(' + tmall_url[j].date + ')'
            history_list = {'history': history}
            history_tmall.append(history_list)
        data_tmall_ctf = {'url':tmall[i].url,'name':tmall[i].name,'price':tmall[i].price,'date':tmall[i].date,"history":history_tmall,'num':len(history_tmall)}
        list_tmall_ctf.append(data_tmall_ctf)
    return render(request, 'lshq_tmall_ctf.html', {'form_ctf_tmall':list_tmall_ctf})
def lshq_css(request):
    list_jd_css = []
    jd = jdprice.objects.filter(shop__contains='周生生').order_by('-date')
    date = [line['date'] for line in jd]
    dates = list(set(date))
    date_now = 0
    for i in range(len(date)):
        if date[i] == dates[len(dates) - 1]:
            date_now += 1
    for i in range(date_now):
        history_jd = []
        jd_url = jdprice.objects.filter(url=jd[i].url).order_by('-date')
        for j in range(len(jd_url)):
            history = jd_url[j].price + '(' + jd_url[j].date + ')'
            history_list = {'history': history}
            history_jd.append(history_list)
        data_jd_css = {'url':jd[i].url,'name':jd[i].name,'price':jd[i].price,'date':jd[i].date,"history":history_jd,'num':len(history_jd)}
        list_jd_css.append(data_jd_css)
    return render(request, 'lshq_css.html', {'form_css_jd':list_jd_css})
def lshq_css_tmall(request):
    list_tmall_css = []
    tmall = tmallprice.objects.filter(shop__contains='周生生').order_by('-date')
    date = [line['date'] for line in tmall]
    dates = list(set(date))
    date_now = 0
    for i in range(len(date)):
        if date[i] == dates[len(dates) - 1]:
            date_now += 1
    for i in range(date_now):
        history_tmall = []
        url = re.split(r'=', tmall[i].url)
        id = re.split(r'&', url[1])[0]
        tmall_url = tmallprice.objects.filter(url__contains=id).order_by('-date')
        for j in range(len(tmall_url)):
            history = tmall_url[j].price + '(' + tmall_url[j].date + ')'
            history_list = {'history': history}
            history_tmall.append(history_list)
        data_tmall_css = {'url':tmall[i].url,'name':tmall[i].name,'price':tmall[i].price,'date':tmall[i].date,"history":history_tmall,'num':len(history_tmall)}
        list_tmall_css.append(data_tmall_css)
    return render(request, 'lshq_tmall_css.html', {'form_css_tmall':list_tmall_css})
def hqzs_sge(request):
    list_sge = []
    sge = sgeprice.objects.filter(source='sge').order_by('-date')
    for i in range(len(sge)):
        Au95 = re.split('/', sge[i].Au95)
        Au95_avg = float(Au95[4])
        Au99 = re.split('/', sge[i].Au99)
        Au99_avg = float(Au99[4])
        Au100 = re.split('/', sge[i].Au100)
        Au100_avg = float(Au100[4])
        iAu99 = re.split('/', sge[i].iAu99)
        iAu99_avg = float(iAu99[4])
        AuTD = re.split('/', sge[i].AuTD)
        AuTD_avg = float(AuTD[4])
        AuTN1 = re.split('/', sge[i].AuTN1)
        AuTN1_avg = float(AuTN1[4])
        AuTN2 = re.split('/', sge[i].AuTN2)
        AuTN2_avg = float(AuTN2[4])
        mAuTD = re.split('/', sge[i].mAuTD)
        mAuTD_avg = float(mAuTD[4])
        Pt95 = re.split('/', sge[i].Pt95)
        Pt95_avg = float(Pt95[4])
        if not sge[i].Ag99 == '-':
            Ag99 = re.split('/', sge[i].Ag99)
            Ag99_avg = float(Ag99[4])
        else:
            Ag99_avg = 0
        AgTD = re.split('/', sge[i].AgTD)
        AgTD_avg = float(AgTD[4])
        if not sge[i].PGC =='-':
            PGC = re.split('/', sge[i].PGC)
            PGC_avg = float(PGC[4])
        else:
            PGC_avg = 0
        data_sge = {'Au95_avg': Au95_avg, 'Au99_avg': Au99_avg, 'Au100_avg': Au100_avg,
                    'iAu99_avg': iAu99_avg,
                    'AuTD_avg': AuTD_avg, 'AuTN1_avg': AuTN1_avg, 'AuTN2_avg': AuTN2_avg,
                    'mAuTD_avg': mAuTD_avg,
                    'Pt95_avg': Pt95_avg, 'Ag99_avg': Ag99_avg, 'AgTD_avg': AgTD_avg, 'PGC_avg': PGC_avg,
                    'date': sge[i].date}
        list_sge.append(data_sge)
    Au95_price = [ line['Au95_avg'] for line in list_sge]
    Au99_price = [ line['Au99_avg'] for line in list_sge]
    Au100_price = [ line['Au100_avg'] for line in list_sge]
    iAu99_price = [ line['iAu99_avg'] for line in list_sge]
    AuTD_price = [ line['AuTD_avg'] for line in list_sge]
    AuTN1_price = [ line['AuTN1_avg'] for line in list_sge]
    AuTN2_price = [ line['AuTN2_avg'] for line in list_sge]
    mAuTD_price = [ line['mAuTD_avg'] for line in list_sge]
    Pt95_price = [ line['Pt95_avg'] for line in list_sge]
    Ag99_price = [ line['Ag99_avg'] for line in list_sge]
    AgTD_price = [ line['AgTD_avg'] for line in list_sge]
    PGC_price = [ line['PGC_avg'] for line in list_sge]
    date = [ line['date'] for line in list_sge]
    bar = Bar(width=798,height=420)
    bar.add("Au99.95", date, Au95_price, is_more_utils=True)
    bar.add("Au99.99",date,Au99_price, is_more_utils=True)
    bar.add("Au100g", date, Au100_price, is_more_utils=True)
    bar.add("iAu99.99", date, iAu99_price, is_more_utils=True)
    bar.add("Au(T+D)", date, AuTD_price, is_more_utils=True)
    bar.add("Au(T+N1)", date, AuTN1_price, is_more_utils=True)
    bar.add("Au(T+N2)", date, AuTN2_price, is_more_utils=True)
    bar.add("mAu(T+D)", date, mAuTD_price, is_more_utils=True)
    bar.add("Pt99.95", date, Pt95_price, is_more_utils=True)
    bar.add("Ag99.99", date, Ag99_price, is_more_utils=True)
    bar.add("Ag(T+D)", date, AgTD_price, is_more_utils=True)
    bar.add("PGC30g", date, PGC_price, is_more_utils=True)
    data = {'data':bar.render_embed()}
    return render(request,'hqzs_sge.html',data)
def hqzs_ctf(request):
    list_jd_ctf = []
    list_tmall_ctf = []
    jd_ctf = jdinfo.objects.filter(shop='周大福').order_by('-date')
    tmall_ctf = tmallinfo.objects.filter(shop='周大福').order_by('-date')
    for i in range(len(jd_ctf)):
        ctf_jd = re.split(r' ',jd_ctf[i].info)
        jd_price_ctf = float(re.split('元/g',ctf_jd[1])[0])
        data_jd_ctf = {'price':jd_price_ctf,'date':jd_ctf[i].date}
        list_jd_ctf.append(data_jd_ctf)
    for i in range(len(tmall_ctf)):
        ctf_tmall = re.split(r' ', tmall_ctf[i].info)
        tmall_price_ctf = float(re.split('元/g', ctf_tmall[2])[0])
        data_tmall_ctf = {'price':tmall_price_ctf,'date':tmall_ctf[i].date}
        list_tmall_ctf.append(data_tmall_ctf)
    jd_ctf_price = [line['price'] for line in list_jd_ctf]
    tmall_ctf_price = [line['price'] for line in list_tmall_ctf]
    date_jd = [line['date'] for line in list_jd_ctf]
    date_tmall = [line['date'] for line in list_tmall_ctf]
    bar = Bar(width=798, height=420)
    bar.add("京东",date_jd,jd_ctf_price,is_more_utils=True)
    bar.add("天猫", date_tmall, tmall_ctf_price, is_more_utils=True)
    data = {'data': bar.render_embed()}
    return render(request,'hqzs_ctf.html',data)
def hqzs_css(request):
    list_tmall_css = []
    tmall_css = tmallinfo.objects.filter(shop='周生生').order_by('-date')
    for i in range(len(tmall_css)):
        css_tmall = re.split(r' ', tmall_css[i].info)
        tmall_price_css = float(css_tmall[1])
        data_tmall_css = {'price': tmall_price_css, 'date': tmall_css[i].date}
        list_tmall_css.append(data_tmall_css)
    tmall_css_price = [line['price'] for line in list_tmall_css]
    date_tmall = [line['date'] for line in list_tmall_css]
    bar = Bar(width=798, height=420)
    bar.add("天猫", date_tmall, tmall_css_price, is_more_utils=True)
    data = {'data': bar.render_embed()}
    return render(request,'hqzs_css.html',data)
def jrhq(request):
    sge = sgejrhq.objects.filter().order_by('date')
    i = len(sge)-1
    Au95 = re.split(r'-',sge[i].Au95)
    Au95_new = Au95[0]
    Au95_high = Au95[1]
    Au95_low = Au95[2]
    Au95_start = Au95[3]
    Au99 = re.split(r'-', sge[i].Au99)
    Au99_new = Au99[0]
    Au99_high = Au99[1]
    Au99_low = Au99[2]
    Au99_start = Au99[3]
    Au100 = re.split(r'-', sge[i].Au100)
    Au100_new = Au100[0]
    Au100_high = Au100[1]
    Au100_low = Au100[2]
    Au100_start = Au100[3]
    iAu99 = re.split(r'-', sge[i].iAu99)
    iAu99_new = iAu99[0]
    iAu99_high = iAu99[1]
    iAu99_low = iAu99[2]
    iAu99_start = iAu99[3]
    AuTD = re.split(r'-', sge[i].AuTD)
    AuTD_new = AuTD[0]
    AuTD_high = AuTD[1]
    AuTD_low = AuTD[2]
    AuTD_start = AuTD[3]
    AuTN1 = re.split(r'-', sge[i].AuTN1)
    AuTN1_new = AuTN1[0]
    AuTN1_high = AuTN1[1]
    AuTN1_low = AuTN1[2]
    AuTN1_start = AuTN1[3]
    AuTN2 = re.split(r'-', sge[i].AuTN2)
    AuTN2_new = AuTN2[0]
    AuTN2_high = AuTN2[1]
    AuTN2_low = AuTN2[2]
    AuTN2_start = AuTN2[3]
    mAuTD = re.split(r'-', sge[i].mAuTD)
    mAuTD_new = mAuTD[0]
    mAuTD_high = mAuTD[1]
    mAuTD_low = mAuTD[2]
    mAuTD_start = mAuTD[3]
    Pt95 = re.split(r'-', sge[i].Pt95)
    Pt95_new = Pt95[0]
    Pt95_high = Pt95[1]
    Pt95_low = Pt95[2]
    Pt95_start = Pt95[3]
    Ag99 = re.split(r'-', sge[i].Ag99)
    Ag99_new = Ag99[0]
    Ag99_high = Ag99[1]
    Ag99_low = Ag99[2]
    Ag99_start = Ag99[3]
    AgTD = re.split(r'-', sge[i].AgTD)
    AgTD_new = AgTD[0]
    AgTD_high = AgTD[1]
    AgTD_low = AgTD[2]
    AgTD_start = AgTD[3]
    PGC = re.split(r'-', sge[i].PGC)
    PGC_new = PGC[0]
    PGC_high = PGC[1]
    PGC_low = PGC[2]
    PGC_start = PGC[3]
    data_sge_jrhq = {'Au95_start': Au95_start, 'Au99_start': Au99_start, 'Au100_start': Au100_start,
                'iAu99_start': iAu99_start, 'AuTD_start': AuTD_start, 'AuTN1_start': AuTN1_start,
                'AuTN2_start': AuTN2_start,'mAuTD_start': mAuTD_start, 'Pt95_start': Pt95_start,
                'Ag99_start': Ag99_start, 'AgTD_start': AgTD_start,'PGC_start': PGC_start,
                'Au95_high': Au95_high, 'Au99_high': Au99_high, 'Au100_high': Au100_high,
                'iAu99_high': iAu99_high, 'AuTD_high': AuTD_high, 'AuTN1_high': AuTN1_high,
                'AuTN2_high': AuTN2_high, 'mAuTD_high': mAuTD_high, 'Pt95_high': Pt95_high,
                'Ag99_high': Ag99_high, 'AgTD_high': AgTD_high, 'PGC_high': PGC_high,
                'Au95_low': Au95_low, 'Au99_low': Au99_low, 'Au100_low': Au100_low,
                'iAu99_low': iAu99_low, 'AuTD_low': AuTD_low, 'AuTN1_low': AuTN1_low,
                'AuTN2_low': AuTN2_low, 'mAuTD_low': mAuTD_low, 'Pt95_low': Pt95_low,
                'Ag99_low': Ag99_low, 'AgTD_low': AgTD_low, 'PGC_low': PGC_low,
                'Au95_new': Au95_new, 'Au99_new': Au99_new, 'Au100_new': Au100_new,
                'iAu99_new': iAu99_new, 'AuTD_new': AuTD_new, 'AuTN1_new': AuTN1_new,
                'AuTN2_new': AuTN2_new, 'mAuTD_new': mAuTD_new, 'Pt95_new': Pt95_new,
                'Ag99_new': Ag99_new, 'AgTD_new': AgTD_new, 'PGC_new': PGC_new,
                'title':sge[i].title,'date':sge[i].date}
    return render(request, 'jrhq.html',{'jrhq': data_sge_jrhq})
def goldprice(request):
    sge = sgejrhq.objects.filter().order_by('date')
    i = len(sge) - 1
    Au95 = re.split(r'-', sge[i].Au95)
    Au95_new = Au95[0]
    Au95_high = Au95[1]
    Au95_low = Au95[2]
    Au95_start = Au95[3]
    Au99 = re.split(r'-', sge[i].Au99)
    Au99_new = Au99[0]
    Au99_high = Au99[1]
    Au99_low = Au99[2]
    Au99_start = Au99[3]
    Au100 = re.split(r'-', sge[i].Au100)
    Au100_new = Au100[0]
    Au100_high = Au100[1]
    Au100_low = Au100[2]
    Au100_start = Au100[3]
    iAu99 = re.split(r'-', sge[i].iAu99)
    iAu99_new = iAu99[0]
    iAu99_high = iAu99[1]
    iAu99_low = iAu99[2]
    iAu99_start = iAu99[3]
    AuTD = re.split(r'-', sge[i].AuTD)
    AuTD_new = AuTD[0]
    AuTD_high = AuTD[1]
    AuTD_low = AuTD[2]
    AuTD_start = AuTD[3]
    AuTN1 = re.split(r'-', sge[i].AuTN1)
    AuTN1_new = AuTN1[0]
    AuTN1_high = AuTN1[1]
    AuTN1_low = AuTN1[2]
    AuTN1_start = AuTN1[3]
    AuTN2 = re.split(r'-', sge[i].AuTN2)
    AuTN2_new = AuTN2[0]
    AuTN2_high = AuTN2[1]
    AuTN2_low = AuTN2[2]
    AuTN2_start = AuTN2[3]
    mAuTD = re.split(r'-', sge[i].mAuTD)
    mAuTD_new = mAuTD[0]
    mAuTD_high = mAuTD[1]
    mAuTD_low = mAuTD[2]
    mAuTD_start = mAuTD[3]
    Pt95 = re.split(r'-', sge[i].Pt95)
    Pt95_new = Pt95[0]
    Pt95_high = Pt95[1]
    Pt95_low = Pt95[2]
    Pt95_start = Pt95[3]
    Ag99 = re.split(r'-', sge[i].Ag99)
    Ag99_new = Ag99[0]
    Ag99_high = Ag99[1]
    Ag99_low = Ag99[2]
    Ag99_start = Ag99[3]
    AgTD = re.split(r'-', sge[i].AgTD)
    AgTD_new = AgTD[0]
    AgTD_high = AgTD[1]
    AgTD_low = AgTD[2]
    AgTD_start = AgTD[3]
    PGC = re.split(r'-', sge[i].PGC)
    PGC_new = PGC[0]
    PGC_high = PGC[1]
    PGC_low = PGC[2]
    PGC_start = PGC[3]
    data_sge_jrhq = {'Au95_start': Au95_start, 'Au99_start': Au99_start, 'Au100_start': Au100_start,
                     'iAu99_start': iAu99_start, 'AuTD_start': AuTD_start, 'AuTN1_start': AuTN1_start,
                     'AuTN2_start': AuTN2_start, 'mAuTD_start': mAuTD_start, 'Pt95_start': Pt95_start,
                     'Ag99_start': Ag99_start, 'AgTD_start': AgTD_start, 'PGC_start': PGC_start,
                     'Au95_high': Au95_high, 'Au99_high': Au99_high, 'Au100_high': Au100_high,
                     'iAu99_high': iAu99_high, 'AuTD_high': AuTD_high, 'AuTN1_high': AuTN1_high,
                     'AuTN2_high': AuTN2_high, 'mAuTD_high': mAuTD_high, 'Pt95_high': Pt95_high,
                     'Ag99_high': Ag99_high, 'AgTD_high': AgTD_high, 'PGC_high': PGC_high,
                     'Au95_low': Au95_low, 'Au99_low': Au99_low, 'Au100_low': Au100_low,
                     'iAu99_low': iAu99_low, 'AuTD_low': AuTD_low, 'AuTN1_low': AuTN1_low,
                     'AuTN2_low': AuTN2_low, 'mAuTD_low': mAuTD_low, 'Pt95_low': Pt95_low,
                     'Ag99_low': Ag99_low, 'AgTD_low': AgTD_low, 'PGC_low': PGC_low,
                     'Au95_new': Au95_new, 'Au99_new': Au99_new, 'Au100_new': Au100_new,
                     'iAu99_new': iAu99_new, 'AuTD_new': AuTD_new, 'AuTN1_new': AuTN1_new,
                     'AuTN2_new': AuTN2_new, 'mAuTD_new': mAuTD_new, 'Pt95_new': Pt95_new,
                     'Ag99_new': Ag99_new, 'AgTD_new': AgTD_new, 'PGC_new': PGC_new,
                     'title': sge[i].title, 'date': sge[i].date}
    bar = Bar(width=500, height=220)
    bar.add("最新价格", ["Au99.95","Au99.99","Au100","iAu99.99","Au(T+D)","Ag99.99"], [Au95_new,Au99_new,Au100_new,iAu99_new,
            AuTD_new,Ag99_new ])
    return render(request, 'goldprice.html', {'jrhq': data_sge_jrhq,'data':bar.render_embed()})
def sge_rec(request):
    return render(request, 'sge_rec.html',{})
def css_rec(request):
    return render(request, 'css_rec.html',{})
def ctf_rec(request):
    return render(request, 'ctf_rec.html',{})