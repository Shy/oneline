import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER
from .styles import Heading
from .models import Person, Line
from .db import DB
from sqlalchemy.orm import sessionmaker
from datetime import date


db = DB.create()
engine = db.engine
Session = sessionmaker(bind=engine)
session = Session()


class oneLine(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))
        person = session.query(Person).first()
        today = date.today()
        lines = (
            session.query(Line)
            .filter_by(person=person.id)
            .filter_by(line_date=today)
            .all()
        )

        if lines:
            line_message = (
                f"You've written {len(lines)} lines! Take a look at what you did!"
            )
        else:
            line_message = "You haven't written any lines yet! Make today your first!"

        welcome_heading = toga.Label(
            f"Welcome back {person.username}!",
            style=Heading.style,
        )
        date_heading = toga.Label(
            line_message,
            style=Pack(direction=ROW, text_align=CENTER, padding=5, font_size=22.4),
        )

        self.name_input = toga.TextInput(style=Pack(flex=1))

        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(self.name_input)

        button = toga.Button(
            f"Submit {today}", on_press=self.save_line, style=Pack(padding=5)
        )

        main_box.add(welcome_heading)
        main_box.add(date_heading)
        main_box.add(name_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def save_line(self):
        session.add(Line(person=self.person.id, line=self.name_input.value))
        print(f"Hello, {self.name_input.value}")


def main():
    return oneLine()
