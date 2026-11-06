from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label



class CharacterScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        layout.add_widget(Label(text="Выбор персонажа", font_size=24, size_hint_y=0.2))
        
        characters = [
            ("Воин", "воин"), 
            ("Маг", "маг"), 
            ("Плут", "плут"), 
            ("Варвар", "варвар")
        ]
        
        for text, char_id in characters:
            btn = Button(text=text, font_size=20)
            btn.bind(on_release=lambda instance, cid=char_id: self.select_character(cid))
            layout.add_widget(btn)
            
        self.add_widget(layout)

    def select_character(self, character):
        app = App.get_running_app()
        app.game_data['character'] = character
        self.manager.current = 'destination'



class DestinationScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        layout.add_widget(Label(text="Куда отправится ваш персонаж?", font_size=24, size_hint_y=0.2))
        
        destinations = [
            ("В таверну", "таверну"), 
            ("В гильдию", "гильдию"), 
            ("В данж к гоблинам", "данж к гоблинам")
        ]
        
        for text, dest_id in destinations:
            btn = Button(text=text, font_size=20)
            btn.bind(on_release=lambda instance, did=dest_id: self.select_destination(did))
            layout.add_widget(btn)
            
        self.add_widget(layout)

    def select_destination(self, destination):
        app = App.get_running_app()
        app.game_data['destination'] = destination
        
        story_screen = self.manager.get_screen('story')
        story_screen.generate_story(app.game_data['character'], app.game_data['destination'])
        
        self.manager.current = 'story'



class StoryScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20)
        

        self.story_label = Label(
            text="", 
            font_size=18, 
            halign='center', 
            valign='middle',
            text_size=(400, None)
        )
        layout.add_widget(self.story_label)
        self.add_widget(layout)

    def generate_story(self, character, destination):
        text = f"Вы выбрали роль: {character.capitalize()}.\n\n"
        text += f"Ваш герой направляется в {destination}.\n\n"
        
        if destination == "таверну":
            text += "Внутри пахнет элем и жареным мясом. За дальним столиком вы замечаете странного незнакомца, который пристально наблюдает за вами. Приключения начинаются..."
        elif destination == "гильдию":
            text += "На доске объявлений висит свежий контракт с огромной наградой. Глава гильдии оценивающе смотрит на вас. Готовы ли вы к первому заданию?.."
        else:
            text += "Сырость и крики зеленых тварей встречают вас у входа в пещеру. Обнажив оружие, вы делаете шаг в темноту данжа..."
            
        self.story_label.text = text

class TextQuestApp(App):
    def build(self):
        self.game_data = {'character': '', 'destination': ''}
        
        sm = ScreenManager()
        sm.add_widget(CharacterScreen(name='character'))
        sm.add_widget(DestinationScreen(name='destination'))
        sm.add_widget(StoryScreen(name='story'))
        
        return sm


if __name__ == '__main__':
    TextQuestApp().run()from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label



class CharacterScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        layout.add_widget(Label(text="Выбор персонажа", font_size=24, size_hint_y=0.2))
        
        characters = [
            ("Воин", "воин"), 
            ("Маг", "маг"), 
            ("Плут", "плут"), 
            ("Варвар", "варвар")
        ]
        
        for text, char_id in characters:
            btn = Button(text=text, font_size=20)
            btn.bind(on_release=lambda instance, cid=char_id: self.select_character(cid))
            layout.add_widget(btn)
            
        self.add_widget(layout)

    def select_character(self, character):
        app = App.get_running_app()
        app.game_data['character'] = character
        self.manager.current = 'destination'



class DestinationScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        layout.add_widget(Label(text="Куда отправится ваш персонаж?", font_size=24, size_hint_y=0.2))
        
        destinations = [
            ("В таверну", "таверну"), 
            ("В гильдию", "гильдию"), 
            ("В данж к гоблинам", "данж к гоблинам")
        ]
        
        for text, dest_id in destinations:
            btn = Button(text=text, font_size=20)
            btn.bind(on_release=lambda instance, did=dest_id: self.select_destination(did))
            layout.add_widget(btn)
            
        self.add_widget(layout)

    def select_destination(self, destination):
        app = App.get_running_app()
        app.game_data['destination'] = destination
        
        story_screen = self.manager.get_screen('story')
        story_screen.generate_story(app.game_data['character'], app.game_data['destination'])
        
        self.manager.current = 'story'



class StoryScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20)
        

        self.story_label = Label(
            text="", 
            font_size=18, 
            halign='center', 
            valign='middle',
            text_size=(400, None)
        )
        layout.add_widget(self.story_label)
        self.add_widget(layout)

    def generate_story(self, character, destination):
        text = f"Вы выбрали роль: {character.capitalize()}.\n\n"
        text += f"Ваш герой направляется в {destination}.\n\n"
        
        if destination == "таверну":
            text += "Внутри пахнет элем и жареным мясом. За дальним столиком вы замечаете странного незнакомца, который пристально наблюдает за вами. Приключения начинаются..."
        elif destination == "гильдию":
            text += "На доске объявлений висит свежий контракт с огромной наградой. Глава гильдии оценивающе смотрит на вас. Готовы ли вы к первому заданию?.."
        else:
            text += "Сырость и крики зеленых тварей встречают вас у входа в пещеру. Обнажив оружие, вы делаете шаг в темноту данжа..."
            
        self.story_label.text = text

class TextQuestApp(App):
    def build(self):
        self.game_data = {'character': '', 'destination': ''}
        
        sm = ScreenManager()
        sm.add_widget(CharacterScreen(name='character'))
        sm.add_widget(DestinationScreen(name='destination'))
        sm.add_widget(StoryScreen(name='story'))
        
        return sm


if __name__ == '__main__':
    TextQuestApp().run()