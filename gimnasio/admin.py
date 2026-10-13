from django.contrib import admin

from gimnasio.models import Plan, Socio


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
	list_display = ("nombre", "duracion_dias", "precio_formateado", "activo")
	list_filter = ("activo", "duracion_dias")
	search_fields = ("nombre", "descripcion")

	@admin.display(description="Precio (CLP)")
	def precio_formateado(self, obj):
		if obj.precio is None:
			return "—"
		return f"${obj.precio:,.0f}".replace(",", ".")


@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
	list_display = (
		"nombre",
		"apellido",
		"correo",
		"plan",
		"fecha_inscripcion",
		"mensualidad_formateada",
	)
	list_filter = ("plan", "fecha_inscripcion")
	search_fields = ("nombre", "apellido", "correo")

	@admin.display(description="Mensualidad (CLP)")
	def mensualidad_formateada(self, obj):
		if obj.mensualidad is None:
			return "—"
		return f"${obj.mensualidad:,.0f}".replace(",", ".")
