from django.http import HttpResponse
import openpyxl


def export_to_xlsx(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="contacts.xlsx"'

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(['Name', 'Last_name', 'Email', 'Phone', 'Address', 'Group'])

    for obj in queryset:
        ws.append([obj.name, obj.last_name, obj.email, obj.phone, obj.address, obj.group])

    wb.save(response)
    return response


export_to_xlsx.short_description = "Export to XLSX"