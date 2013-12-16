import itertools
from django.views.generic import ListView
from uerp.apps.ppc.models import ProcessPPCDayReport


class PPCDayReport(ListView):
    model = ProcessPPCDayReport
    template_name = 'templates/ppc/day_report.html'
    queryset = ProcessPPCDayReport.objects.all().order_by('partner_id', 'campaign', 'date')

    def get_context_data(self, **kwargs):
        context = super(PPCDayReport, self).get_context_data(**kwargs)
        dates = list(set([i.date for i in self.queryset]))
        dates.sort()
        context['dates'] = dates
        report = []
        for partner, i in itertools.groupby(self.queryset, lambda x: x.partner_id):

            for campaign, j in itertools.groupby(i, lambda x: x.campaign):
                record = {
                    'partner': partner,
                    'campaign': campaign,
                }
                record_dates = {}
                for item in j:
                    if not record.get('specialist'):
                        record['specialist'] = item.specialist
                    if not record.get('service'):
                        record['service'] = item.service_id
                    if not record.get('domain_zone'):
                        record['domain_zone'] = item.domain_zone
                    record_dates[item.date] = item.cash
                for date in dates:
                    if not record_dates.get(date):
                        record_dates[date] = '-'
                record['dates'] = sorted([{'date': d, 'cash': c} for d, c in record_dates.items()], key=lambda d: d['date'])
                report.append(record)
        context['report_list'] = report
        return context