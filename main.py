from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.label import Label
from kivy.storage.jsonstore import JsonStore

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.properties import ListProperty, BooleanProperty
from kivy.properties import NumericProperty


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


class RV(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_data()
        Clock.schedule_interval(self.load_data, 1)
    
    def load_data(self, *args):
        store = JsonStore('data.json')
        data_list = []
        for item in store:
            data_list.append({'text': item})
        self.data = data_list


class ToDoView(BoxLayout):
    def delete_row(self):
        value = RecycleViewRow().check.active
        if value:
            self.remove_widget(RecycleViewRow().check.active)
        print("5")


class DisorderBanisherApp(App):
    def build(self):
        return ToDoView()


if __name__ == '__main__':
    DisorderBanisherApp().run()