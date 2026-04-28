import flet as ft
from datetime import datetime


class AppMorbimortalidad:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Morbimortalidad — Videotoracoscopia"
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.theme = ft.Theme(
            color_scheme_seed="#0a2463",
            font_family="Roboto",
        )
        self.page.padding = 0
        self.page.scroll = ft.ScrollMode.ALWAYS
        self.page.bgcolor = "#eef2f7"
        
        # Optimizaciones para móvil Android
        self.page.window_width = 400
        self.page.window_height = 850
        self.page.window_resizable = False

        self.pacientes = []
        self.resultado_visible = False

        # Colores
        self.AZUL = "#0a2463"
        self.AZUL_MEDIO = "#1e3a78"
        self.AZUL_CLARO = "#3d6098"
        self.AZUL_SUAVE = "#e8edf5"
        self.FONDO_CARD = "#ffffff"
        self.GRIS_CLARO = "#f4f6f9"
        self.TEXTO = "#1a1a2e"
        self.TEXTO_SECUNDARIO = "#5a6178"
        self.VERDE = "#1b8754"
        self.VERDE_FONDO = "#e6f7ee"
        self.ROJO = "#c0392b"
        self.ROJO_FONDO = "#fdecea"
        self.AMARILLO_FONDO = "#fef9e7"
        self.AMARILLO_BORDE = "#f0c944"
        self.ACENTO = "#1a73e8"

        # Estilo para inputs
        inp_style = {
            "text_size": 14,
            "border_radius": 10,
            "border_color": "#d0d5dd",
            "focused_border_color": self.ACENTO,
            "bgcolor": "#f8f9fc",
            "content_padding": ft.padding.symmetric(10, 14),
        }
        drop_style = {
            "text_size": 14,
            "border_radius": 10,
            "border_color": "#d0d5dd",
            "focused_border_color": self.ACENTO,
            "bgcolor": "#f8f9fc",
            "content_padding": ft.padding.symmetric(10, 14),
        }

        # Variables del formulario
        self.historia = ft.TextField(label="Historia Clínica N°", width=300,
                                    autofocus=True, **inp_style)
        self.nombre = ft.TextField(label="Nombre del paciente", width=300, **inp_style)
        self.edad = ft.TextField(label="Edad", width=150,
                                keyboard_type=ft.KeyboardType.NUMBER, **inp_style)
        self.sexo = ft.Dropdown(label="Sexo", width=150, options=[
            ft.dropdown.Option("Masculino"), ft.dropdown.Option("Femenino")], **drop_style)
        self.peso = ft.TextField(label="Peso (kg)", width=150,
                                keyboard_type=ft.KeyboardType.NUMBER, **inp_style)
        self.talla = ft.TextField(label="Talla (cm)", width=150,
                                 keyboard_type=ft.KeyboardType.NUMBER, **inp_style)
        self.imc = ft.TextField(label="IMC", width=150, read_only=True,
                                value="", border_color="#c8cdd5",
                                border_radius=10, bgcolor="#eceff4",
                                text_size=14, content_padding=ft.padding.symmetric(10, 14))
        self.spo2 = ft.TextField(label="SpO2 preop (%)", width=150,
                                keyboard_type=ft.KeyboardType.NUMBER, **inp_style)
        self.hemo = ft.TextField(label="Hemoglobina (g/dL)", width=150,
                                keyboard_type=ft.KeyboardType.NUMBER, **inp_style)
        self.albumina = ft.TextField(label="Albumina (g/dL)", width=150,
                                    keyboard_type=ft.KeyboardType.NUMBER, **inp_style)
        self.asa = ft.Dropdown(label="Clase ASA", width=150, options=[
            ft.dropdown.Option("ASA I"), ft.dropdown.Option("ASA II"),
            ft.dropdown.Option("ASA III"), ft.dropdown.Option("ASA IV"),
            ft.dropdown.Option("ASA V")], **drop_style)
        self.nutricion = ft.Dropdown(label="Estado nutricional", width=150, options=[
            ft.dropdown.Option("Normal"), ft.dropdown.Option("Sobrepeso"),
            ft.dropdown.Option("Obesidad"), ft.dropdown.Option("Desnutrido")], **drop_style)

        chk_style = {
            "fill_color": self.ACENTO,
            "check_color": "#ffffff",
            "active_color": self.ACENTO,
        }
        self.tabaco = ft.Checkbox(label="Tabaco", **chk_style)
        self.alcohol = ft.Checkbox(label="Alcohol", **chk_style)
        self.drogas = ft.Checkbox(label="Drogas", **chk_style)
        self.hta = ft.Checkbox(label="HTA", **chk_style)
        self.dm = ft.Checkbox(label="DM", **chk_style)
        self.epoc = ft.Checkbox(label="EPOC", **chk_style)
        self.cardiopatia = ft.Checkbox(label="Cardiopatía", **chk_style)
        self.nefropatia = ft.Checkbox(label="Nefropatía", **chk_style)
        self.hepatopatia = ft.Checkbox(label="Hepatopatía", **chk_style)

        self.proceder = ft.Dropdown(label="Tipo de proceder", width=300, options=[
            ft.dropdown.Option("Biopsia pulmonar"), ft.dropdown.Option("Lobectomía"),
            ft.dropdown.Option("Neumonectomía"), ft.dropdown.Option("Pleurectomía"),
            ft.dropdown.Option("Pericardiectomía"), ft.dropdown.Option("Esofagectomía"),
            ft.dropdown.Option("Tumorectomía"), ft.dropdown.Option("Otro")], **drop_style)
        self.tiempo_qx = ft.TextField(label="Tiempo quirúrgico (min)", width=150,
                                      keyboard_type=ft.KeyboardType.NUMBER, **inp_style)
        self.conversion = ft.Dropdown(label="Conversión a toracotomía", width=150, options=[
            ft.dropdown.Option("No"), ft.dropdown.Option("Sí")], **drop_style)
        self.derrame = ft.Dropdown(label="Derrame pleural", width=150, options=[
            ft.dropdown.Option("No"), ft.dropdown.Option("Leve"),
            ft.dropdown.Option("Moderado"), ft.dropdown.Option("Severo")], **drop_style)
        self.localizacion = ft.Dropdown(label="Localización", width=150, options=[
            ft.dropdown.Option("Lóbulo sup. derecho"), ft.dropdown.Option("Lóbulo medio derecho"),
            ft.dropdown.Option("Lóbulo inf. derecho"), ft.dropdown.Option("Lóbulo sup. izquierdo"),
            ft.dropdown.Option("Lóbulo inf. izquierdo"), ft.dropdown.Option("Bilateral"),
            ft.dropdown.Option("Mediastino"), ft.dropdown.Option("Pleura")], **drop_style)
        self.hemorragia = ft.TextField(label="Hemorragia intraop (mL)", width=150,
                                       keyboard_type=ft.KeyboardType.NUMBER, **inp_style)
        self.anestesia = ft.Dropdown(label="Tipo de anestesia", width=150, options=[
            ft.dropdown.Option("General"), ft.dropdown.Option("General + Epidural"),
            ft.dropdown.Option("Local + Sedación")], **drop_style)
        self.intubacion = ft.Dropdown(label="Intubación selectiva", width=150, options=[
            ft.dropdown.Option("Sí"), ft.dropdown.Option("No")], **drop_style)
        self.reoperacion = ft.Dropdown(label="Reoperación", width=150, options=[
            ft.dropdown.Option("No"), ft.dropdown.Option("Sí")], **drop_style)

        # Resultado
        self.lbl_valor = ft.Text("--", size=36, weight=ft.FontWeight.BOLD,
                                 color=self.AZUL, text_align=ft.TextAlign.CENTER)
        self.lbl_badge = ft.Text("", size=14, weight=ft.FontWeight.BOLD,
                                 text_align=ft.TextAlign.CENTER)
        self.resultado_container = ft.Container(
            visible=False, padding=16,
            bgcolor=self.AMARILLO_FONDO,
            border=ft.border.all(2, self.AMARILLO_BORDE),
            border_radius=14,
            content=ft.Column([
                self.lbl_valor,
                ft.Text("Probabilidad de Morbimortalidad (%)",
                        size=12, text_align=ft.TextAlign.CENTER,
                        color=self.TEXTO_SECUNDARIO),
                self.lbl_badge,
                ft.Container(height=1, bgcolor=self.AMARILLO_BORDE,
                            margin=ft.margin.symmetric(vertical=6)),
                ft.Row([
                    ft.Container(width=14, height=14, bgcolor=self.ROJO, border_radius=7),
                    ft.Text(" Prob. Alta (68-100)", size=12, weight=ft.FontWeight.BOLD, color=self.ROJO)
                ]),
                ft.Row([
                    ft.Container(width=14, height=14, bgcolor=self.VERDE, border_radius=7),
                    ft.Text(" Prob. Baja (1-67.9)", size=12, weight=ft.FontWeight.BOLD, color=self.VERDE)
                ]),
            ], alignment=ft.MainAxisAlignment.CENTER,
               horizontal_alignment=ft.CrossAxisAlignment.CENTER))

        # Tabla
        self.tabla = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("HC", weight=ft.FontWeight.BOLD, size=11, color=self.AZUL)),
                ft.DataColumn(ft.Text("Paciente", weight=ft.FontWeight.BOLD, size=11, color=self.AZUL)),
                ft.DataColumn(ft.Text("Edad", weight=ft.FontWeight.BOLD, size=11, color=self.AZUL)),
                ft.DataColumn(ft.Text("ASA", weight=ft.FontWeight.BOLD, size=11, color=self.AZUL)),
                ft.DataColumn(ft.Text("Prob.", weight=ft.FontWeight.BOLD, size=11, color=self.AZUL)),
                ft.DataColumn(ft.Text("Clasif.", weight=ft.FontWeight.BOLD, size=11, color=self.AZUL)),
            ],
            rows=[],
            column_spacing=4,
            heading_row_height=32,
            data_row_min_height=38,
            horizontal_margin=4,
            heading_row_color=self.AZUL_SUAVE,
        )

        self.lbl_contador = ft.Text("Total: 0 pacientes", size=12,
                                    color=self.TEXTO_SECUNDARIO, italic=True)
        self.lbl_num_pacientes = ft.Text("0", size=11, color="#ffffff",
                                         weight=ft.FontWeight.BOLD)

        # IMC automático
        self.peso.on_change = self._calc_imc
        self.talla.on_change = self._calc_imc

        # Construir interfaz con panel dividido
        self._construir_interfaz()

    def _construir_interfaz(self):
        # Panel de ayuda (lateral derecho en escritorio, abajo en móvil)
        panel_ayuda = self._crear_panel_ayuda()
        
        # Row principal que permite scroll horizontal en móvil
        main_row = ft.Row(
            [
                # Columna del formulario
                ft.Column([
                    self._crear_header(),
                    ft.Container(height=8),
                    self._crear_formulario(),
                ], scroll=ft.ScrollMode.ALWAYS, expand=2),
                # Columna de ayuda (visible en escritorio, colapsable en móvil)
                ft.Column([
                    panel_ayuda
                ], expand=1, scroll=ft.ScrollMode.ALWAYS),
            ],
            vertical_alignment=ft.CrossAxisAlignment.START,
            spacing=8,
        )
        
        self.page.add(main_row)

    def _crear_header(self):
        return ft.Container(
            content=ft.Column([
                ft.Text("Morbimortalidad", size=20, weight=ft.FontWeight.BOLD,
                        color="#ffffff"),
                ft.Text("Videotoracoscopia", size=12, color="#b0c4de"),
            ], spacing=2),
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=[self.AZUL, self.AZUL_MEDIO, self.AZUL_CLARO]
            ),
            padding=ft.padding.symmetric(16, 20),
            border_radius=ft.border_radius.only(bottom_left=20, bottom_right=20),
        )

    def _crear_formulario(self):
        return ft.Container(
            content=ft.Column([
                ft.Container(content=self.historia, padding=4),
                ft.Container(content=self.nombre, padding=4),
                
                # Sección Clínicas
                self._seccion("Variables Clínicas", [
                    ft.Row([self.edad, self.sexo], spacing=6),
                    ft.Row([self.peso, self.talla], spacing=6),
                    ft.Row([self.imc, self.spo2], spacing=6),
                    ft.Row([self.hemo, self.albumina], spacing=6),
                    ft.Row([self.asa, self.nutricion], spacing=6),
                    ft.Container(height=4),
                    ft.Text("Hábitos tóxicos", size=12, weight=ft.FontWeight.W_600,
                            color=self.TEXTO_SECUNDARIO),
                    ft.Row([self.tabaco, self.alcohol, self.drogas], spacing=8, wrap=True),
                    ft.Container(height=4),
                    ft.Text("Comorbilidades", size=12, weight=ft.FontWeight.W_600,
                            color=self.TEXTO_SECUNDARIO),
                    ft.Row([self.hta, self.dm, self.epoc], spacing=8, wrap=True),
                    ft.Row([self.cardiopatia, self.nefropatia, self.hepatopatia], spacing=8, wrap=True),
                ]),

                ft.Container(height=8),

                # Sección Quirúrgicas
                self._seccion("Variables Quirúrgicas", [
                    self.proceder,
                    ft.Row([self.tiempo_qx, self.conversion], spacing=6),
                    ft.Row([self.derrame, self.localizacion], spacing=6),
                    ft.Row([self.hemorragia, self.anestesia], spacing=6),
                    ft.Row([self.intubacion, self.reoperacion], spacing=6),
                ]),

                ft.Container(height=12),

                # Botones
                ft.Row([
                    ft.ElevatedButton(
                        "Calcular y Guardar",
                        bgcolor=self.AZUL,
                        color="#ffffff",
                        style=ft.ButtonStyle(
                            padding=ft.padding.symmetric(12, 20),
                            shape=ft.RoundedRectangleBorder(radius=12),
                            text_style=ft.TextStyle(size=14, weight=ft.FontWeight.W_600),
                        ),
                        on_click=self.calcular_y_guardar,
                    ),
                    ft.OutlinedButton(
                        "Limpiar",
                        border_color="#c0c5d0",
                        color=self.TEXTO_SECUNDARIO,
                        style=ft.ButtonStyle(
                            padding=ft.padding.symmetric(12, 16),
                            shape=ft.RoundedRectangleBorder(radius=12),
                            text_style=ft.TextStyle(size=14, weight=ft.FontWeight.W_600),
                        ),
                        on_click=self.limpiar,
                    ),
                    ft.OutlinedButton(
                        "Eliminar",
                        border_color=self.ROJO,
                        color=self.ROJO,
                        style=ft.ButtonStyle(
                            padding=ft.padding.symmetric(12, 16),
                            shape=ft.RoundedRectangleBorder(radius=12),
                            text_style=ft.TextStyle(size=14, weight=ft.FontWeight.W_600),
                        ),
                        on_click=self.eliminar_seleccionado,
                    ),
                ], alignment=ft.MainAxisAlignment.CENTER, spacing=10),

                ft.Container(height=12),

                self.resultado_container,

                ft.Container(height=8),

                # Tabla de pacientes
                self._crear_tabla_pacientes(),

            ], spacing=4),
            padding=ft.padding.symmetric(14, 12),
        )

    def _seccion(self, titulo, controles):
        return ft.Container(
            content=ft.Column([
                ft.Container(
                    content=ft.Text(titulo, size=14, weight=ft.FontWeight.W_600,
                                    color="#ffffff"),
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.center_left,
                        end=ft.alignment.center_right,
                        colors=[self.AZUL_MEDIO, self.AZUL_CLARO]
                    ),
                    padding=ft.padding.symmetric(12, 14),
                    border_radius=ft.border_radius.only(top_left=12, top_right=12),
                ),
                ft.Container(
                    content=ft.Column(controles, spacing=6),
                    bgcolor=self.FONDO_CARD,
                    padding=12,
                    border_radius=ft.border_radius.only(bottom_left=12, bottom_right=12),
                    shadow=ft.BoxShadow(
                        spread_radius=0, blur_radius=6,
                        offset=ft.Offset(0, 2), color="#0a246312"
                    ),
                ),
            ], spacing=0)
        )

    def _crear_panel_ayuda(self):
        """Panel de ayuda lateral con descripciones de ASA, IMC y más"""
        return ft.Container(
            content=ft.Column([
                ft.Text("📋 GUÍA DE AYUDA", size=14, weight=ft.FontWeight.BOLD,
                        color=self.AZUL, text_align=ft.TextAlign.CENTER),
                ft.Container(height=8),
                
                self._seccion_ayuda("🏥 Clasificación ASA",
                    "• ASA I: Paciente sano normal\n"
                    "• ASA II: Enfermedad sistémica leve\n"
                    "• ASA III: Enfermedad sistémica grave\n"
                    "• ASA IV: Enfermedad incapacitante (riesgo vital)\n"
                    "• ASA V: Moribundo (no se espera sobrevida sin cirugía)"),
                
                self._seccion_ayuda("⚖️ Índice de Masa Corporal (IMC)",
                    "Fórmula: Peso (kg) / Talla² (m²)\n\n"
                    "• < 18.5: Bajo peso\n"
                    "• 18.5 - 24.9: Normal\n"
                    "• 25 - 29.9: Sobrepeso\n"
                    "• ≥ 30: Obesidad"),
                
                self._seccion_ayuda("🎯 Interpretación del Resultado",
                    "• PROBABILIDAD BAJA (<68%): Riesgo bajo de morbimortalidad.\n\n"
                    "• PROBABILIDAD ALTA (≥68%): Riesgo elevado de complicaciones.\n"
                    "  Considerar cuidados intensivos, monitoreo estrecho."),
                
                self._seccion_ayuda("⚠️ Factores de mayor peso",
                    "• Neumonectomía: +18 pts\n"
                    "• ASA IV: +16 pts\n"
                    "• Edad ≥70: +14 pts\n"
                    "• Cardiopatía: +10 pts\n"
                    "• Reoperación: +10 pts\n"
                    "• Desnutrición: +12 pts"),
                
                self._seccion_ayuda("📝 Cómo usar",
                    "1. Complete todos los campos\n"
                    "2. El IMC se calcula automáticamente\n"
                    "3. Presione 'Calcular y Guardar'\n"
                    "4. El riesgo se muestra en porcentaje\n"
                    "5. Los pacientes quedan en la tabla\n"
                    "6. Toque en tabla para ver detalle"),
            ], spacing=6, scroll=ft.ScrollMode.ALWAYS),
            bgcolor=self.GRIS_CLARO,
            border_radius=16,
            padding=12,
            width=280,
        )

    def _seccion_ayuda(self, titulo, contenido):
        return ft.Container(
            content=ft.Column([
                ft.Text(titulo, size=12, weight=ft.FontWeight.BOLD,
                        color=self.AZUL_MEDIO),
                ft.Text(contenido, size=10, color=self.TEXTO_SECUNDARIO),
            ], spacing=4),
            bgcolor=self.FONDO_CARD,
            padding=10,
            border_radius=10,
        )

    def _crear_tabla_pacientes(self):
        return ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Text("Pacientes Registrados", size=15,
                            weight=ft.FontWeight.BOLD, color="#ffffff"),
                    ft.Container(width=6),
                    ft.Container(
                        content=self.lbl_num_pacientes,
                        bgcolor=self.AZUL_CLARO,
                        padding=ft.padding.symmetric(4, 8),
                        border_radius=10,
                    ),
                ]),
                ft.Container(height=8),
                ft.Container(
                    content=ft.Column(
                        [self.tabla],
                        scroll=ft.ScrollMode.HORIZONTAL,
                    ),
                    bgcolor=self.FONDO_CARD,
                    border_radius=12,
                    padding=4,
                ),
                ft.Container(height=8),
                self.lbl_contador,
            ]),
            padding=16,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=[self.AZUL, self.AZUL_MEDIO]
            ),
            border_radius=16,
        )

    def _calc_imc(self, e=None):
        try:
            p = float(self.peso.value or 0)
            t = float(self.talla.value or 0)
            if p > 0 and t > 0:
                self.imc.value = f"{p / ((t/100)**2):.1f}"
            else:
                self.imc.value = ""
        except (ValueError, TypeError):
            self.imc.value = ""
        self.imc.update()

    def _obtener(self, campo):
        v = campo.value if hasattr(campo, 'value') else ""
        return v.strip() if isinstance(v, str) else v

    def _calcular_probabilidad(self):
        p = 0
        try:
            edad = int(self.edad.value or 0)
        except (ValueError, TypeError):
            edad = 0

        if edad >= 70:    p += 14
        elif edad >= 60:  p += 10
        elif edad >= 50:  p += 6
        else:             p += 2

        p += 4 if self.sexo.value == "Masculino" else 2
        if self.tabaco.value:      p += 6
        if self.alcohol.value:     p += 4
        if self.drogas.value:      p += 8
        if self.hta.value:         p += 5
        if self.dm.value:          p += 5
        if self.epoc.value:        p += 8
        if self.cardiopatia.value: p += 10
        if self.nefropatia.value:  p += 7
        if self.hepatopatia.value: p += 6

        p += {"ASA I": 2, "ASA II": 5, "ASA III": 10,
              "ASA IV": 16, "ASA V": 22}.get(self.asa.value, 0)
        p += {"Normal": 0, "Sobrepeso": 3, "Obesidad": 7,
              "Desnutrido": 12}.get(self.nutricion.value, 0)

        try:
            h = float(self.hemo.value or 0)
            if h < 10:    p += 10
            elif h < 12:  p += 5
        except (ValueError, TypeError):
            pass

        try:
            a = float(self.albumina.value or 0)
            if a < 2.5:   p += 10
            elif a < 3.5: p += 5
        except (ValueError, TypeError):
            pass

        try:
            s = float(self.spo2.value or 0)
            if s < 90:    p += 10
            elif s < 95:  p += 5
        except (ValueError, TypeError):
            pass

        p += {"Biopsia pulmonar": 3, "Pleurectomía": 5, "Tumorectomía": 5,
              "Pericardiectomía": 6, "Lobectomía": 10, "Esofagectomía": 14,
              "Neumonectomía": 18, "Otro": 6}.get(self.proceder.value, 5)

        try:
            t = int(self.tiempo_qx.value or 0)
            if t > 240:    p += 12
            elif t > 180:  p += 8
            elif t > 120:  p += 5
            else:           p += 2
        except (ValueError, TypeError):
            pass

        if self.conversion.value == "Sí": p += 12
        p += {"No": 0, "Leve": 2, "Moderado": 5, "Severo": 8}.get(self.derrame.value, 0)

        try:
            hg = float(self.hemorragia.value or 0)
            if hg > 1000:    p += 12
            elif hg > 500:   p += 7
            elif hg > 200:   p += 3
        except (ValueError, TypeError):
            pass

        an = self.anestesia.value
        if an == "Local + Sedación": p += 1
        elif an == "General":         p += 4
        else:                         p += 2

        if self.intubacion.value == "No":  p += 5
        if self.reoperacion.value == "Sí": p += 10

        return max(1, min(100, round((p / 190) * 100)))

    def calcular_y_guardar(self, e=None):
        # Validaciones
        if not self._obtener(self.historia):
            self._mostrar_snackbar("Ingrese el número de Historia Clínica", self.ROJO)
            return
        if not self._obtener(self.nombre):
            self._mostrar_snackbar("Ingrese el nombre del paciente", self.ROJO)
            return

        obligatorios = [
            (self.edad, "Edad"), (self.sexo, "Sexo"), (self.asa, "Clase ASA"),
            (self.nutricion, "Estado nutricional"), (self.proceder, "Tipo de proceder"),
            (self.tiempo_qx, "Tiempo quirúrgico"), (self.conversion, "Conversión"),
            (self.anestesia, "Tipo de anestesia"), (self.intubacion, "Intubación selectiva"),
            (self.reoperacion, "Reoperación"),
        ]
        for campo, nombre in obligatorios:
            if not self._obtener(campo):
                self._mostrar_snackbar(f"Complete el campo: {nombre}", self.ROJO)
                return

        prob = self._calcular_probabilidad()
        clasif = "ALTA" if prob >= 68 else "BAJA"
        ahora = datetime.now().strftime("%d/%m/%Y %H:%M")

        paciente = {
            "historia": self.historia.value,
            "nombre": self.nombre.value,
            "edad": self.edad.value,
            "sexo": self.sexo.value,
            "asa": self.asa.value,
            "proceder": self.proceder.value,
            "probabilidad": prob,
            "clasificacion": clasif,
            "fecha": ahora,
            "peso": self.peso.value,
            "talla": self.talla.value,
            "imc": self.imc.value,
            "spo2": self.spo2.value,
            "hemo": self.hemo.value,
            "albumina": self.albumina.value,
            "nutricion": self.nutricion.value,
            "tiempo_qx": self.tiempo_qx.value,
            "conversion": self.conversion.value,
            "derrame": self.derrame.value,
            "localizacion": self.localizacion.value,
            "hemorragia": self.hemorragia.value,
            "anestesia": self.anestesia.value,
            "intubacion": self.intubacion.value,
            "reoperacion": self.reoperacion.value,
            "toxicos": {
                "Tabaco": self.tabaco.value,
                "Alcohol": self.alcohol.value,
                "Drogas": self.drogas.value,
            },
            "comorbilidades": {
                "HTA": self.hta.value,
                "DM": self.dm.value,
                "EPOC": self.epoc.value,
                "Cardiopatía": self.cardiopatia.value,
                "Nefropatía": self.nefropatia.value,
                "Hepatopatía": self.hepatopatia.value,
            },
        }

        self.pacientes.append(paciente)

        # Agregar fila a la tabla
        bgcolor = self.ROJO_FONDO if clasif == "ALTA" else self.VERDE_FONDO
        color = self.ROJO if clasif == "ALTA" else self.VERDE
        
        self.tabla.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(paciente["historia"], size=11)),
                    ft.DataCell(ft.Text(paciente["nombre"], size=11, weight=ft.FontWeight.W_500)),
                    ft.DataCell(ft.Text(paciente["edad"], size=11)),
                    ft.DataCell(ft.Text(paciente["asa"], size=11)),
                    ft.DataCell(ft.Text(f"{prob}%", size=11, weight=ft.FontWeight.BOLD,
                                       color=color)),
                    ft.DataCell(ft.Text(clasif, size=11, weight=ft.FontWeight.BOLD,
                                       color=color)),
                ],
                on_long_press=lambda e, idx=len(self.pacientes)-1: self._ver_detalle(idx),
                on_click=lambda e, idx=len(self.pacientes)-1: self._ver_detalle(idx),
            )
        )

        self._mostrar_resultado(prob, clasif)
        self.lbl_contador.value = f"Total: {len(self.pacientes)} pacientes"
        self.lbl_num_pacientes.value = str(len(self.pacientes))
        self._mostrar_snackbar(f"Guardado: {paciente['nombre']} - {prob}% {clasif}", self.VERDE)
        self.page.update()

    def _ver_detalle(self, idx):
        pac = self.pacientes[idx]
        
        toxicos = ", ".join(k for k, v in pac["toxicos"].items() if v) or "Ninguno"
        comorb = ", ".join(k for k, v in pac["comorbilidades"].items() if v) or "Ninguna"
        
        contenido = ft.Column([
            ft.Text(f"Paciente: {pac['nombre']}", size=16, weight=ft.FontWeight.BOLD),
            ft.Text(f"Historia Clínica: {pac['historia']}", size=12),
            ft.Text(f"Fecha: {pac['fecha']}", size=11, italic=True),
            ft.Divider(),
            ft.Text("Variables Clínicas", weight=ft.FontWeight.BOLD, size=14),
            ft.Text(f"Edad: {pac['edad']} años"),
            ft.Text(f"Sexo: {pac['sexo']}"),
            ft.Text(f"IMC: {pac['imc']}"),
            ft.Text(f"SpO2: {pac['spo2']}%"),
            ft.Text(f"Hemoglobina: {pac['hemo']} g/dL"),
            ft.Text(f"Albúmina: {pac['albumina']} g/dL"),
            ft.Text(f"ASA: {pac['asa']}"),
            ft.Text(f"Nutrición: {pac['nutricion']}"),
            ft.Text(f"Hábitos tóxicos: {toxicos}"),
            ft.Text(f"Comorbilidades: {comorb}"),
            ft.Divider(),
            ft.Text("Variables Quirúrgicas", weight=ft.FontWeight.BOLD, size=14),
            ft.Text(f"Proceder: {pac['proceder']}"),
            ft.Text(f"Tiempo Qx: {pac['tiempo_qx']} min"),
            ft.Text(f"Conversión: {pac['conversion']}"),
            ft.Text(f"Derrame: {pac['derrame']}"),
            ft.Text(f"Hemorragia: {pac['hemorragia']} mL"),
            ft.Divider(),
            ft.Text(f"RESULTADO: {pac['probabilidad']}% — {pac['clasificacion']}",
                   size=14, weight=ft.FontWeight.BOLD,
                   color=self.ROJO if pac['clasificacion'] == "ALTA" else self.VERDE),
        ], spacing=5, scroll=ft.ScrollMode.ALWAYS)
        
        dialog = ft.AlertDialog(
            title=ft.Text(f"Detalle - {pac['nombre']}"),
            content=ft.Container(content=contenido, width=350, height=450),
            actions=[ft.TextButton("Cerrar", on_click=lambda e: self.close_dialog(dialog))],
        )
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()
    
    def close_dialog(self, dialog):
        dialog.open = False
        self.page.update()

    def eliminar_seleccionado(self, e=None):
        if not self.pacientes:
            self._mostrar_snackbar("No hay pacientes para eliminar", self.ROJO)
            return
        
        # Crear dialog de selección
        opciones = ft.Column([
            ft.Text("Seleccione el paciente a eliminar:", size=12),
            ft.Divider(),
        ])
        
        for i, p in enumerate(self.pacientes):
            opciones.controls.append(
                ft.ElevatedButton(
                    f"{p['historia']} - {p['nombre']} ({p['probabilidad']}%)",
                    on_click=lambda e, idx=i: self._confirmar_eliminacion(idx),
                    style=ft.ButtonStyle(bgcolor=self.GRIS_CLARO),
                )
            )
        
        opciones.controls.append(ft.TextButton("Cancelar", on_click=lambda e: self.close_dialog(dialog)))
        
        dialog = ft.AlertDialog(
            title=ft.Text("Eliminar Paciente"),
            content=ft.Container(content=opciones, width=300, height=300),
        )
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()
    
    def _confirmar_eliminacion(self, idx):
        paciente = self.pacientes.pop(idx)
        self.tabla.rows.pop(idx)
        self.lbl_contador.value = f"Total: {len(self.pacientes)} pacientes"
        self.lbl_num_pacientes.value = str(len(self.pacientes))
        self.page.dialog.open = False
        self._mostrar_snackbar(f"Eliminado: {paciente['nombre']}", self.ROJO)
        self.page.update()

    def _mostrar_resultado(self, prob, clasif):
        self.lbl_valor.value = f"{prob}%"
        if clasif == "ALTA":
            self.lbl_badge.value = "⚠️ PROBABILIDAD ALTA ⚠️"
            self.lbl_badge.color = self.ROJO
        else:
            self.lbl_badge.value = "✅ PROBABILIDAD BAJA ✅"
            self.lbl_badge.color = self.VERDE
        self.resultado_container.visible = True
        self.resultado_visible = True
        self.page.update()

    def _mostrar_snackbar(self, mensaje, color):
        self.page.snack_bar = ft.SnackBar(
            ft.Text(mensaje, color="#ffffff", weight=ft.FontWeight.W_500),
            bgcolor=color,
        )
        self.page.snack_bar.open = True
        self.page.update()

    def limpiar(self, e=None):
        self.historia.value = ""
        self.nombre.value = ""
        self.edad.value = ""
        self.sexo.value = None
        self.peso.value = ""
        self.talla.value = ""
        self.imc.value = ""
        self.spo2.value = ""
        self.hemo.value = ""
        self.albumina.value = ""
        self.asa.value = None
        self.nutricion.value = None
        self.tabaco.value = False
        self.alcohol.value = False
        self.drogas.value = False
        self.hta.value = False
        self.dm.value = False
        self.epoc.value = False
        self.cardiopatia.value = False
        self.nefropatia.value = False
        self.hepatopatia.value = False
        self.proceder.value = None
        self.tiempo_qx.value = ""
        self.conversion.value = None
        self.derrame.value = None
        self.localizacion.value = None
        self.hemorragia.value = ""
        self.anestesia.value = None
        self.intubacion.value = None
        self.reoperacion.value = None
        self.resultado_container.visible = False
        self.resultado_visible = False
        self.page.update()


def main(page: ft.Page):
    AppMorbimortalidad(page)

