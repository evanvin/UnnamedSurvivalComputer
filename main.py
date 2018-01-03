# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.uix.image import Image

from kivymd.bottomsheet import MDListBottomSheet, MDGridBottomSheet
from kivymd.button import MDIconButton
from kivymd.date_picker import MDDatePicker
from kivymd.dialog import MDDialog
from kivymd.label import MDLabel
from kivymd.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch, BaseListItem
from kivymd.material_resources import DEVICE_TYPE
from kivymd.navigationdrawer import MDNavigationDrawer, NavigationDrawerHeaderBase
from kivymd.selectioncontrols import MDCheckbox
from kivymd.snackbar import Snackbar
from kivymd.theming import ThemeManager
from kivymd.time_picker import MDTimePicker

main_widget_kv = '''
#:import Toolbar kivymd.toolbar.Toolbar
#:import ThemeManager kivymd.theming.ThemeManager
#:import MDNavigationDrawer kivymd.navigationdrawer.MDNavigationDrawer
#:import NavigationLayout kivymd.navigationdrawer.NavigationLayout
#:import NavigationDrawerDivider kivymd.navigationdrawer.NavigationDrawerDivider
#:import NavigationDrawerToolbar kivymd.navigationdrawer.NavigationDrawerToolbar
#:import NavigationDrawerSubheader kivymd.navigationdrawer.NavigationDrawerSubheader
#:import MDCheckbox kivymd.selectioncontrols.MDCheckbox
#:import MDSwitch kivymd.selectioncontrols.MDSwitch
#:import MDList kivymd.list.MDList
#:import OneLineListItem kivymd.list.OneLineListItem
#:import TwoLineListItem kivymd.list.TwoLineListItem
#:import ThreeLineListItem kivymd.list.ThreeLineListItem
#:import OneLineAvatarListItem kivymd.list.OneLineAvatarListItem
#:import OneLineIconListItem kivymd.list.OneLineIconListItem
#:import OneLineAvatarIconListItem kivymd.list.OneLineAvatarIconListItem
#:import MDTextField kivymd.textfields.MDTextField
#:import MDSpinner kivymd.spinner.MDSpinner
#:import MDCard kivymd.card.MDCard
#:import MDSeparator kivymd.card.MDSeparator
#:import MDDropdownMenu kivymd.menu.MDDropdownMenu
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import colors kivymd.color_definitions.colors
#:import SmartTile kivymd.grid.SmartTile
#:import MDSlider kivymd.slider.MDSlider
#:import MDTabbedPanel kivymd.tabs.MDTabbedPanel
#:import MDTab kivymd.tabs.MDTab
#:import MDProgressBar kivymd.progressbar.MDProgressBar
#:import MDAccordion kivymd.accordion.MDAccordion
#:import MDAccordionItem kivymd.accordion.MDAccordionItem
#:import MDAccordionSubItem kivymd.accordion.MDAccordionSubItem
#:import MDThemePicker kivymd.theme_picker.MDThemePicker
#:import MDBottomNavigation kivymd.tabs.MDBottomNavigation
#:import MDBottomNavigationItem kivymd.tabs.MDBottomNavigationItem

NavigationLayout:
    id: nav_layout
    MDNavigationDrawer:
        id: nav_drawer
        NavigationDrawerToolbar:
            title: "Topics"
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Animals"
            on_release: app.root.ids.scr_mngr.current = 'animals'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Camouflage"
            on_release: app.root.ids.scr_mngr.current = 'camouflage'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Cold Weather"
            on_release: app.root.ids.scr_mngr.current = 'cold_weather'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Dangerous Arthropods"
            on_release: app.root.ids.scr_mngr.current = 'dangerous_arthropods'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Desert"
            on_release: app.root.ids.scr_mngr.current = 'desert'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Direction Finding"
            on_release: app.root.ids.scr_mngr.current = 'direction_finding'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Fire"
            on_release: app.root.ids.scr_mngr.current = 'fire'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Fish & Mollusks"
            on_release: app.root.ids.scr_mngr.current = 'fish_mollusks'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Food"
            on_release: app.root.ids.scr_mngr.current = 'food'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Hostile Areas"
            on_release: app.root.ids.scr_mngr.current = 'hostile_areas'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Kits"
            on_release: app.root.ids.scr_mngr.current = 'kits'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Man-Made Hazards"
            on_release: app.root.ids.scr_mngr.current = 'manmade_hazards'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Medicine"
            on_release: app.root.ids.scr_mngr.current = 'medicine'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Multi Tool"
            on_release: app.root.ids.scr_mngr.current = 'multi_tool'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "People"
            on_release: app.root.ids.scr_mngr.current = 'people'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Planning"
            on_release: app.root.ids.scr_mngr.current = 'planning'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Plants"
            on_release: app.root.ids.scr_mngr.current = 'plants'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Power"
            on_release: app.root.ids.scr_mngr.current = 'power'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Psychology"
            on_release: app.root.ids.scr_mngr.current = 'psychology'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Ropes & Knots"
            on_release: app.root.ids.scr_mngr.current = 'ropes_knots'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Sea"
            on_release: app.root.ids.scr_mngr.current = 'sea'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Shelter"
            on_release: app.root.ids.scr_mngr.current = 'shelter'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Signaling"
            on_release: app.root.ids.scr_mngr.current = 'signaling'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Tools"
            on_release: app.root.ids.scr_mngr.current = 'tools'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Tropical"
            on_release: app.root.ids.scr_mngr.current = 'tropical'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Water"
            on_release: app.root.ids.scr_mngr.current = 'water'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Water Crossing"
            on_release: app.root.ids.scr_mngr.current = 'water_crossing'
    BoxLayout:
        orientation: 'vertical'
        Toolbar:
            id: toolbar
            title: 'Unnamed Survival Computer'
            md_bg_color: app.theme_cls.primary_color
            background_palette: 'Primary'
            background_hue: '500'
            left_action_items: [['menu', lambda x: app.root.toggle_nav_drawer()]]
        ScreenManager:
            id: scr_mngr
            Screen:
                name: 'animals'
                BoxLayout:
                    RstDocument:
                        source: './assets/manual/Animals.rst'
            Screen:
                name: 'camouflage'
                BoxLayout:
                    RstDocument:
                        source: './assets/manual/Camouflage.rst'
            Screen:
                name: 'cold_weather'
                BoxLayout:
                    RstDocument:
                        source: './assets/manual/ColdWeather.rst'
            Screen:
                name: 'dangerous_arthropods'
                BoxLayout:
                    RstDocument:
                        source: './assets/manual/DangerousArthropods.rst'
            Screen:
                name: 'desert'
                BoxLayout:
                    RstDocument:
                        source: './assets/manual/Desert.rst'
            Screen:
                name: 'direction_finding'
                BoxLayout:
                    RstDocument:
                        source: './assets/manual/DirectionFinding.rst'
            Screen:
                name: 'fire'
                BoxLayout:
                    RstDocument:
                        source: './assets/manual/Fire.rst'
            Screen:
                name: 'fish_mollusks'
                BoxLayout:
                    RstDocument:
                        source: './assets/manual/FishAndMollusks.rst'
            Screen:
                name: 'food'
                BoxLayout:
                    RstDocument:
                        source: './assets/manual/Food.rst'
            Screen:
                name: 'hostile_areas'
                BoxLayout:
                    RstDocument:
                        source: './assets/manual/HostileAreas.rst'
            Screen:
                name: 'kits'
                BoxLayout:
                    RstDocument:
                        source: './assets/manual/Kits.rst'
            Screen:
                name: 'manmade_hazards'
                BoxLayout:
                    RstDocument:
                        source: './assets/manual/ManMadeHazards.rst'
            Screen:
                name: 'medicine'
                BoxLayout:
                    RstDocument:
                        source: './assets/manual/Medicine.rst'
            Screen:
                name: 'multi_tool'
                BoxLayout:
                    RstDocument:
                        source: './assets/manual/MultiTool.rst'
            Screen:
                name: 'people'
                BoxLayout:
                    RstDocument:
                        source: './assets/manual/People.rst'
            Screen:
                name: 'planning'
                BoxLayout:
                    RstDocument:
                        source: './assets/manual/planning.rst'
            Screen:
                name: 'plants'
                BoxLayout:
                    RstDocument:
                        source: './assets/manual/plants.rst'
            Screen:
                name: 'power'
                BoxLayout:
                    RstDocument:
                        source: './assets/manual/Power.rst'
            Screen:
                name: 'psychology'
                BoxLayout:
                    RstDocument:
                        source: './assets/manual/psychology.rst'
            Screen:
                name: 'ropes_knots'
                BoxLayout:
                    RstDocument:
                        source: './assets/manual/RopesAndKnots.rst'
            Screen:
                name: 'sea'
                BoxLayout:
                    RstDocument:
                        source: './assets/manual/Sea.rst'
            Screen:
                name: 'shelter'
                BoxLayout:
                    RstDocument:
                        source: './assets/manual/Shelter.rst'
            Screen:
                name: 'signaling'
                BoxLayout:
                    RstDocument:
                        source: './assets/manual/Signaling.rst'
            Screen:
                name: 'tools'
                BoxLayout:
                    RstDocument:
                        source: './assets/manual/Tools.rst'
            Screen:
                name: 'tropical'
                BoxLayout:
                    RstDocument:
                        source: './assets/manual/Tropical.rst'
            Screen:
                name: 'water'
                BoxLayout:
                    RstDocument:
                        source: './assets/manual/Water.rst'
            Screen:
                name: 'water_crossing'
                BoxLayout:
                    RstDocument:
                        source: './assets/manual/WaterCrossing.rst'
            

            

'''


class HackedDemoNavDrawer(MDNavigationDrawer):
    # DO NOT USE
    def add_widget(self, widget, index=0):
        if issubclass(widget.__class__, BaseListItem):
            self._list.add_widget(widget, index)
            if len(self._list.children) == 1:
                widget._active = True
                self.active_item = widget
            # widget.bind(on_release=lambda x: self.panel.toggle_state())
            widget.bind(on_release=lambda x: x._set_active(True, list=self))
        elif issubclass(widget.__class__, NavigationDrawerHeaderBase):
            self._header_container.add_widget(widget)
        else:
            super(MDNavigationDrawer, self).add_widget(widget, index)


class KitchenSink(App):
    theme_cls = ThemeManager()
    previous_date = ObjectProperty()
    title = "Unnamed Survival Computer"

    menu_items = [
        {'viewclass': 'MDMenuItem',
         'text': 'Example item'},
        {'viewclass': 'MDMenuItem',
         'text': 'Example item'},
        {'viewclass': 'MDMenuItem',
         'text': 'Example item'},
        {'viewclass': 'MDMenuItem',
         'text': 'Example item'},
        {'viewclass': 'MDMenuItem',
         'text': 'Example item'},
        {'viewclass': 'MDMenuItem',
         'text': 'Example item'},
        {'viewclass': 'MDMenuItem',
         'text': 'Example item'},
    ]

    def build(self):
        main_widget = Builder.load_string(main_widget_kv)
        self.theme_cls.theme_style = 'Dark'

        return main_widget


    def on_pause(self):
        return True

    def on_stop(self):
        pass


class AvatarSampleWidget(ILeftBody, Image):
    pass


class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
    pass


class IconRightSampleWidget(IRightBodyTouch, MDCheckbox):
    pass


if __name__ == '__main__':
    KitchenSink().run()
