from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.label import Label
from kivy.storage.jsonstore import JsonStore
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

from kivy.clock import Clock
from kivy.lang import Builder

from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.properties import ListProperty, BooleanProperty
from kivy.properties import NumericProperty
from kivy.properties import DictProperty




class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior, RecycleBoxLayout):
    pass
    ''' Adds selection and focus behaviour to the view. '''
#-----------------------------------------------------------------------
class RecycleViewRow(RecycleDataViewBehavior, BoxLayout):
    ''' Add selection support to the Label '''

    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    text = StringProperty('')
    check = ObjectProperty(False)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(RecycleViewRow, self).refresh_view_attrs(
            rv, index, data)

    def set_check_true(self):
        text = self.text
        app = App.get_running_app()
        app.checkbox[f"{text}"] = True

    # def on_touch_down(self, touch):
    #     ''' Add selection on touch down '''
    #     if super(RecycleViewRow, self).on_touch_down(touch):
    #         return True
    #     if self.collide_point(*touch.pos) and self.selectable:
    #         return self.parent.select_with_touch(self.index, touch)

    # def apply_selection(self, rv, index, is_selected):
    #     ''' Respond to the selection of items in the view. '''

    #     self.selected = is_selected

    #     if is_selected:
    #         pass
    #     else:
    #         pass

class AddItemPopup(Popup):
    def add_row(self, **args):
        store = JsonStore('data.json')
        app = App.get_running_app()
        store.put(app.popup_text)
        self.dismiss()

    def print_popup_text(self, *args):
        print(self.popup_text)


class RV(RecycleView):
    selected_row = None
    
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.load_data()
        Clock.schedule_interval(self.load_data, 1)
    
    def load_data(self, *args):
        store = JsonStore('data.json')
        data_list = []
        for item in store:
            data_list.append({'text': item})
        self.data = data_list

    def find_row(self, instance):
        self.selected_row = instance.index


class ToDoView(BoxLayout):
    def show_popup(self, *args):
        p = AddItemPopup()
        app = App.get_running_app()
        p.content.text_input.bind(text=app.setter('popup_text'))
        rview = RV()
        for child in rview.ids['grid'].children:
            print(child, child.id)
        p.open()
    
    def delete_row(self, *args):
        task = App.get_running_app()
        for k, v in task.checkbox.items():
            if v == True:
                store = JsonStore('data.json')
                store.delete(f'{k}')
        rvr = RecycleViewRow()
        rvr.selected = False


class DisorderBanisherApp(App):
    checkbox = {}
    store = JsonStore('data.json')
    i = 0
    for item in store:
        checkbox[f'ch{i}']: False

    popup_text = StringProperty('')

    def build(self):
        return ToDoView()


if __name__ == '__main__':
    DisorderBanisherApp().run()