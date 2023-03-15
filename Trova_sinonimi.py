from kivymd.app import MDApp 
from kivy.lang import Builder 
from kivy.network.urlrequest import UrlRequest
import certifi 
from urllib.parse import quote 
from kivymd.uix.dialog import MDDialog
from kivymd.uix.pickers import MDDatePicker


KV = """

MDNavigationLayout:

    MDScreenManager:

        MDScreen:

            BoxLayout:
                orientation: 'vertical'

                MDTopAppBar:
                    title: "Syno"
                    elevation: 4
                    pos_hint: {"top": 1}
                    md_bg_color: "#000000"
                    specific_text_color: "#ff4d06"
                    left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]

                GridLayout:
                    rows: 3

                    MDTextField:
                        id: mdtext
                        hint_text: 'What are you looking for?' 
                        mode: 'rectangle' 
                        line_color: '#ff4d06'
                        
                        

                    MDRectangleFlatIconButton:
                        text: 'Search!' 
                        icon: 'magnify' 
                        size_hint_x: 1                        
                        size_hint_y: 0.1
                        text_color: '#ff4d06'
                        line_color: '#ff4d06'
                        icon_color: '#ff4d06'
                        on_press: app.search_button() 

                    ScrollView:
                        MDLabel:
                            id: mdlab 
                            text: 'Welcome to Syno!'
                            font_style: 'H3'
                            halign: 'center'
                            padding_y: '50dp'
                            size_hint_y: None 
                            height: self.texture_size[1] 
                            text_size: self.width, None 
                            theme_text_color: 'Custom'
                            text_color: '#ff4d06'
                    
                MDRaisedButton:
                    text: "Set theme"
                    on_release: app.switch_theme_style()
                    size_hint_x: 1
                    md_bg_color: '#ff4d06'
                    
                    

                MDRaisedButton:
                    text: "Date picker"
                    on_release: app.show_date_picker() 
                    size_hint_x: 1   
                    md_bg_color: 'black'                       

    MDNavigationDrawer:
        id: nav_drawer

        BoxLayout:
            orientation: "vertical"
            padding: "8dp"
            spacing: "8dp"

            AnchorLayout:
                anchor_x: "left"
                size_hint_y: None
                height: avatar.height

                Image:
                    id: avatar
                    size_hint: None, None
                    size: "56dp", "56dp"
                    source: "data/logo/kivy-icon-256.png"

            MDLabel:
                text: "Syno App 0.1"
                theme_text_color: 'Custom'
                text_color: '#ff4d06'
                font_style: "Button"
                size_hint_y: None
                height: self.texture_size[1]

            MDLabel:
                text: "prospy93@icloud.com"
                theme_text_color: 'Custom' 
                text_color: '#ff4d06'
                font_style: "Caption"
                size_hint_y: None
                height: self.texture_size[1]

            ScrollView: 

                MDList:

                    OneLineIconListItem:
                        text: "Thanks Python"
                        theme_text_color: 'Custom'
                        text_color: '#ff4d06'
                        on_press: app.press_icon() 
                        

                        IconLeftWidget:
                            icon: "language-python"
                            
                                                                      
"""


class Syno(MDApp):

    info_dialog = None 

    def build(self):
        self.title = 'Syno' 
        self.theme_cls.theme_style_switch_animation = True 
        self.theme_cls.theme_style = 'Dark' 
        self.theme_cls.primary_palette = 'Orange' 
        self.theme_cls.primary_hue = '900' 
        return Builder.load_string(KV) 
    
    def switch_theme_style(self):
        self.theme_cls.primary_palette = (
            'Orange' if self.theme_cls.primary_palette == 'Orange' else 'Orange'
        )
        self.theme_cls.theme_style = (
            'Dark' if self.theme_cls.theme_style == 'Light' else 'Light'
        )
    
    def search_button(self):
        endpoint = "https://api.datamuse.com/words?rel_syn="
        query = self.root.ids['mdtext'].text.strip() 
        encoded_query = quote(query) 
        url = endpoint + encoded_query 
        self.root.ids['mdtext'].text = 'Loading...' 
        self.rs_request = UrlRequest(url,
                                     on_success = self.success_callback,
                                     on_error = self.error_callback,
                                     ca_file = certifi.where()) 
    
    def success_callback(self, request, result): 
        self.root.ids['mdtext'].text = '' 
        words = [] 
        for r in result:
            words.append(r['word']) 
        self.root.ids['mdlab'].text = ', '.join(words) 
    
    def error_callback(self, request, result):
        self.root.ids['mdtext'].text = ''
        self.root.ids['mdlab'].text = 'Word not found' 
        print(result) 

    def press_icon(self):
        app_info = 'This app was built using Python language\n\nand kivyMD framework' 
        if not self.info_dialog:
            self.info_dialog = MDDialog(
                title = 'Info app',
                text = app_info,
                auto_dismiss = True 
            )
        self.info_dialog.open() 
    
    def on_save(self, instance, value, date_range):
        """
        Events called when the OK dialog box button is clicked.
        
        :type instance: <kivymd.uix.picker.MDDatePicker object>;
        :param value: selected date;
        :type value: <class 'datetime.date'>;
        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date range: <class 'list'>;
        """

        print(instance, value, date_range) 

    def on_cancel(self, instance, value):
        "Events called when the 'CANCEL' dialog box button is clicked."

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save = self.on_save, on_cancel = self.on_cancel) 
        date_dialog.open() 
    
    
Syno().run()  
                                     
                                      
    
    
            
            




        


        