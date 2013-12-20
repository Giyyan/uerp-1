import itertools
from django.db.models import Q
from django.views.generic import ListView
from uerp.apps.ppc.models import ProcessPPCDayReport


class PPCDayReport(ListView):
    model = ProcessPPCDayReport
    template_name = 'ppc/day_report.html'

    def get_context_data(self, **kwargs):
        context = super(PPCDayReport, self).get_context_data(**kwargs)
        queryset = self.get_queryset()
        if queryset:
            dates = list(set([i.date for i in queryset if i.date is not None]))
            dates.sort()
            context['dates'] = dates
            report = []
            for partner, i in itertools.groupby(queryset, lambda x: x.partner):
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
                        record_dates[item.date] = item.cash or 0.0
                    for date in dates:
                        if not record_dates.get(date):
                            record_dates[date] = '-'
                    record['dates'] = sorted([{'date': d, 'cash': c} for d, c in record_dates.items()], key=lambda d: d['date'])
                    report.append(record)
            context['report_list'] = report
            context['search'] = {
                'campaign': self.request.REQUEST.get("campaign", ''),
                'partner': self.request.REQUEST.get("partner", ''),
                'date_start': self.request.REQUEST.get("date_start", ''),
                'date_end': self.request.REQUEST.get("date_end", ''),
                'specialist': self.request.REQUEST.get("specialist", ''),
            }
        return context

    def get_queryset(self):
        campaign = self.request.REQUEST.get("campaign")
        partner = self.request.REQUEST.get("partner")
        date_start = self.request.REQUEST.get("date_start")
        date_end = self.request.REQUEST.get("date_end")
        specialist = self.request.REQUEST.get("specialist")
        query = []
        if campaign:
            query.append(Q(campaign=campaign))
        if partner:
            query.append(Q(partner__name__icontains=partner) | Q(partner__ur_name__icontains=partner))
        if date_start:
            query.append(Q(date__gte=date_start))
        if date_end:
            query.append(Q(date__lte=date_end))
        if specialist:
            query.append(Q(specialist__name__icontains=specialist))

        if query:
            queryset = ProcessPPCDayReport.objects.prefetch_related('partner', 'specialist').filter(*query).order_by('partner', 'campaign', 'date')
            return queryset
        return ProcessPPCDayReport.objects.prefetch_related('partner', 'specialist').order_by('partner', 'campaign', 'date')
