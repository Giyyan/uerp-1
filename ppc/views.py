from django.shortcuts import render
from django.views.generic import ListView
import itertools
from ppc.models import ProcessPPCDayReport
from res.models import Employee


class PPCDayReport(ListView):
    model = ProcessPPCDayReport
    template_name = 'ppc/day_report.html'
    queryset = ProcessPPCDayReport.objects.all().order_by('partner_id', 'campaign', 'date')

    def get_context_data(self, **kwargs):
        context = super(PPCDayReport, self).get_context_data(**kwargs)
        dates = list(set([i.date for i in self.queryset]))
        dates.sort()
        context['dates'] = dates
        report = []
        # partners =
        for partner, i in itertools.groupby(self.queryset, lambda x: x.partner_id):
            record = {
                'partner': partner,
                'service': 0,
                'specialist': 0,
                'campaign': 0,
                'domain_zone': 0,
                'dates': []
            }
            for campaign, j in itertools.groupby(i, lambda x: x.campaign):
                record['campaign'] = campaign

                for item in j:
                    if not record['specialist']:
                        record['specialist'] = item.specialist_id
                    if not record['service']:
                        record['service'] = item.service_id
                    if not record['domain_zone']:
                        record['domain_zone'] = item.domain_zone

        return context