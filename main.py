from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class ClickMate(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.click_interval = "Set Time"
        self.mouse_button = "Left"
        self.click_type = "Single"
        self.click_repeat = "Continuous"

    def setupUI(self):
        self.setFixedSize(600, 500)
        self.setWindowTitle("ClickMate")

        self.central_widget = QtWidgets.QWidget(self)

        self.verticalLayout = QtWidgets.QVBoxLayout(self.central_widget)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(5)

        self.click_interval_box = QtWidgets.QGroupBox("Click Interval", self.central_widget)
        self.click_interval_box.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.click_interval_box)
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_10.setSpacing(5)

        self.widget_6 = QtWidgets.QWidget(self.click_interval_box)

        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_6)

        self.set_time_radio = QtWidgets.QRadioButton("Set Time", self.widget_6)
        self.set_time_radio.setChecked(True)
        self.set_time_radio.clicked.connect(lambda: self.onClickIntervalClicked("Set Time"))
        self.horizontalLayout_9.addWidget(self.set_time_radio)

        self.random_interval_radio = QtWidgets.QRadioButton("Random Interval", self.widget_6)
        self.random_interval_radio.setEnabled(True)
        self.random_interval_radio.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.random_interval_radio.clicked.connect(lambda: self.onClickIntervalClicked("Random Interval"))
        self.horizontalLayout_9.addWidget(self.random_interval_radio)

        self.verticalLayout_10.addWidget(self.widget_6)

        self.widget_7 = QtWidgets.QWidget(self.click_interval_box)

        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(20)

        self.widget_8 = QtWidgets.QWidget(self.widget_7)

        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(5)

        self.hours_layout = QtWidgets.QVBoxLayout()
        self.hours_layout.setSpacing(5)

        self.hours_edit = QtWidgets.QLineEdit(self.widget_8)
        self.hours_edit.setPlaceholderText("0")
        self.hours_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.hours_layout.addWidget(self.hours_edit)

        self.hours_label = QtWidgets.QLabel("Hours", self.widget_8)
        self.hours_label.setAlignment(QtCore.Qt.AlignCenter)

        self.hours_layout.addWidget(self.hours_label)
        self.hours_layout.setStretch(0, 2)
        self.hours_layout.setStretch(1, 1)

        self.horizontalLayout_6.addLayout(self.hours_layout)

        self.minutes_layout = QtWidgets.QVBoxLayout()
        self.minutes_layout.setSpacing(5)

        self.minutes_edit = QtWidgets.QLineEdit(self.widget_8)
        self.minutes_edit.setPlaceholderText("0")
        self.minutes_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.minutes_layout.addWidget(self.minutes_edit)

        self.minutes_label = QtWidgets.QLabel("Minutes", self.widget_8)
        self.minutes_label.setAlignment(QtCore.Qt.AlignCenter)
        self.minutes_layout.addWidget(self.minutes_label)

        self.minutes_layout.setStretch(0, 2)
        self.minutes_layout.setStretch(1, 1)

        self.horizontalLayout_6.addLayout(self.minutes_layout)

        self.seconds_layout = QtWidgets.QVBoxLayout()
        self.seconds_layout.setSpacing(5)

        self.seconds_edit = QtWidgets.QLineEdit(self.widget_8)
        self.seconds_edit.setText("1")
        self.seconds_edit.setPlaceholderText("0")
        self.seconds_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.seconds_layout.addWidget(self.seconds_edit)

        self.seconds_label = QtWidgets.QLabel("Seconds", self.widget_8)
        self.seconds_label.setAlignment(QtCore.Qt.AlignCenter)
        self.seconds_layout.addWidget(self.seconds_label)

        self.seconds_layout.setStretch(0, 2)
        self.seconds_layout.setStretch(1, 1)

        self.horizontalLayout_6.addLayout(self.seconds_layout)

        self.milli_layout = QtWidgets.QVBoxLayout()
        self.milli_layout.setSpacing(5)

        self.milli_edit = QtWidgets.QLineEdit(self.widget_8)
        self.milli_edit.setPlaceholderText("0")
        self.milli_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.milli_layout.addWidget(self.milli_edit)

        self.milli_label = QtWidgets.QLabel("Milliseconds", self.widget_8)
        self.milli_label.setAlignment(QtCore.Qt.AlignCenter)
        self.milli_layout.addWidget(self.milli_label)

        self.milli_layout.setStretch(0, 2)
        self.milli_layout.setStretch(1, 1)

        self.horizontalLayout_6.addLayout(self.milli_layout)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)
        self.horizontalLayout_6.setStretch(2, 1)
        self.horizontalLayout_6.setStretch(3, 1)

        self.horizontalLayout_8.addWidget(self.widget_8)

        self.widget_9 = QtWidgets.QWidget(self.widget_7)

        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(5)

        self.from_layout = QtWidgets.QVBoxLayout()
        self.from_layout.setSpacing(5)

        self.from_edit = QtWidgets.QLineEdit(self.widget_9)
        self.from_edit.setPlaceholderText("0")
        self.from_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.from_edit.setEnabled(False)
        self.from_layout.addWidget(self.from_edit)

        self.from_label = QtWidgets.QLabel("Seconds", self.widget_9)
        self.from_label.setAlignment(QtCore.Qt.AlignCenter)
        self.from_layout.addWidget(self.from_label)

        self.from_layout.setStretch(0, 2)
        self.from_layout.setStretch(1, 1)

        self.horizontalLayout_7.addLayout(self.from_layout)

        self.to_layout = QtWidgets.QVBoxLayout()
        self.to_layout.setSpacing(5)

        self.to_edit = QtWidgets.QLineEdit(self.widget_9)
        self.to_edit.setPlaceholderText("0")
        self.to_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.to_edit.setEnabled(False)
        self.to_layout.addWidget(self.to_edit)

        self.to_label = QtWidgets.QLabel("Seconds", self.widget_9)
        self.to_label.setAlignment(QtCore.Qt.AlignCenter)
        self.to_layout.addWidget(self.to_label)

        self.to_layout.setStretch(0, 2)
        self.to_layout.setStretch(1, 1)

        self.horizontalLayout_7.addLayout(self.to_layout)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 1)

        self.horizontalLayout_8.addWidget(self.widget_9)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 1)

        self.verticalLayout_10.addWidget(self.widget_7)

        self.verticalLayout_10.setStretch(0, 1)
        self.verticalLayout_10.setStretch(1, 2)

        self.verticalLayout.addWidget(self.click_interval_box)

        self.widget = QtWidgets.QWidget(self.central_widget)

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(5)

        self.click_option_box = QtWidgets.QGroupBox("Click Options", self.widget)
        self.click_option_box.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.click_option_box)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setSpacing(5)

        self.mouse_button_label = QtWidgets.QLabel("Mouse Button", self.click_option_box)
        self.verticalLayout_2.addWidget(self.mouse_button_label)

        self.widget_3 = QtWidgets.QWidget(self.click_option_box)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(5)

        self.left_button = QtWidgets.QPushButton("Left", self.widget_3)
        self.left_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.left_button.setCheckable(True)
        self.left_button.setChecked(True)
        self.left_button.clicked.connect(lambda: self.onMouseButtonClicked("Left"))
        self.horizontalLayout_3.addWidget(self.left_button)

        self.middle_button = QtWidgets.QPushButton("Middle", self.widget_3)
        self.middle_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.middle_button.setCheckable(True)
        self.middle_button.clicked.connect(lambda: self.onMouseButtonClicked("Middle"))
        self.horizontalLayout_3.addWidget(self.middle_button)

        self.right_button = QtWidgets.QPushButton("Right", self.widget_3)
        self.right_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.right_button.setCheckable(True)
        self.right_button.clicked.connect(lambda: self.onMouseButtonClicked("Right"))
        self.horizontalLayout_3.addWidget(self.right_button)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)

        self.verticalLayout_2.addWidget(self.widget_3)

        self.click_type_label = QtWidgets.QLabel("Click Type", self.click_option_box)
        self.verticalLayout_2.addWidget(self.click_type_label)

        self.widget_4 = QtWidgets.QWidget(self.click_option_box)

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(5)

        self.single_button = QtWidgets.QPushButton("Single", self.widget_4)
        self.single_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.single_button.setCheckable(True)
        self.single_button.setChecked(True)
        self.single_button.clicked.connect(lambda: self.onClickTypeClicked("Single"))
        self.horizontalLayout_4.addWidget(self.single_button)

        self.double_button = QtWidgets.QPushButton("Double", self.widget_4)
        self.double_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.double_button.setCheckable(True)
        self.double_button.clicked.connect(lambda: self.onClickTypeClicked("Double"))
        self.horizontalLayout_4.addWidget(self.double_button)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)

        self.verticalLayout_2.addWidget(self.widget_4)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 1)

        self.horizontalLayout.addWidget(self.click_option_box)

        self.click_repeat_box = QtWidgets.QGroupBox("Click Repeat", self.widget)
        self.click_repeat_box.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.click_repeat_box)
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setSpacing(5)

        self.limited_radio = QtWidgets.QRadioButton("Limited", self.click_repeat_box)
        self.limited_radio.clicked.connect(lambda: self.onClickRepeatClicked("Limited"))
        self.verticalLayout_3.addWidget(self.limited_radio)

        self.widget_5 = QtWidgets.QWidget(self.click_repeat_box)

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_5.setSpacing(5)

        self.clicks_edit = QtWidgets.QLineEdit(self.widget_5)
        self.clicks_edit.setPlaceholderText("0")
        self.clicks_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.clicks_edit.setEnabled(False)
        self.horizontalLayout_5.addWidget(self.clicks_edit)

        self.clicks_label = QtWidgets.QLabel("Clicks", self.widget_5)
        self.clicks_label.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout_5.addWidget(self.clicks_label)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout_3.addWidget(self.widget_5)

        self.continuous_radio = QtWidgets.QRadioButton("Continuous", self.click_repeat_box)
        self.continuous_radio.setChecked(True)
        self.continuous_radio.clicked.connect(lambda: self.onClickRepeatClicked("Continuous"))
        self.verticalLayout_3.addWidget(self.continuous_radio)

        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 2)

        self.horizontalLayout.addWidget(self.click_repeat_box)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QtWidgets.QWidget(self.central_widget)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(5)

        self.start_button = QtWidgets.QPushButton("Start", self.widget_2)
        self.start_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_button.clicked.connect(self.onStartClicked)
        self.horizontalLayout_2.addWidget(self.start_button)

        self.stop_button = QtWidgets.QPushButton("Stop", self.widget_2)
        self.stop_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stop_button.setEnabled(False)
        self.stop_button.clicked.connect(self.onStopClicked)
        self.horizontalLayout_2.addWidget(self.stop_button)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout.addWidget(self.widget_2)

        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 1)

        self.setCentralWidget(self.central_widget)

        self.setInputValidator()

    def onStartClicked(self):
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.click_interval_box.setEnabled(False)
        self.widget.setEnabled(False)

    def onStopClicked(self):
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.click_interval_box.setEnabled(True)
        self.widget.setEnabled(True)

    def setInputValidator(self):
        input_fields = [self.hours_edit, self.minutes_edit, self.seconds_edit, self.milli_edit, self.from_edit, self.to_edit, self.clicks_edit]

        validator = QtGui.QIntValidator()
        validator.setBottom(0)
        validator.setTop(1000)

        for field in input_fields:
            field.setValidator(validator)

    def onClickIntervalClicked(self, click_interval):
        self.click_interval = click_interval
        self.seconds_edit.setText("1")

        if click_interval == "Set Time":
            enable_time_fields = [self.hours_edit, self.minutes_edit, self.seconds_edit, self.milli_edit]
            clear_time_fields = [self.from_edit, self.to_edit]
            disable_time_fields = [self.from_edit, self.to_edit]
        elif click_interval == "Random Interval":
            enable_time_fields = [self.from_edit, self.to_edit]
            clear_time_fields = [self.hours_edit, self.minutes_edit, self.milli_edit]
            disable_time_fields = [self.hours_edit, self.minutes_edit, self.seconds_edit, self.milli_edit]

        for field in enable_time_fields:
            field.setEnabled(True)

        for field in disable_time_fields:
            field.setEnabled(False)

        for field in clear_time_fields:
            field.clear()

    def onMouseButtonClicked(self, mouse_button):
        button_mapping = {"Left": self.left_button, "Middle": self.middle_button, "Right": self.right_button}

        if self.mouse_button != mouse_button:
            self.mouse_button = mouse_button
            for button, checkbox in button_mapping.items():
                checkbox.setChecked(button == mouse_button)
        else:
            button_mapping[mouse_button].setChecked(True)

    def onClickTypeClicked(self, click_type):
        button_mapping = {"Single": self.single_button, "Double": self.double_button}

        if self.click_type != click_type:
            self.click_type = click_type
            for button, checkbox in button_mapping.items():
                checkbox.setChecked(button == click_type)
        else:
            button_mapping[click_type].setChecked(True)

    def onClickRepeatClicked(self, click_repeat):
        self.click_repeat = click_repeat

        if click_repeat == "Limited":
            self.clicks_edit.setEnabled(True)
        elif click_repeat == "Continuous":
            self.clicks_edit.setEnabled(False)
            self.clicks_edit.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ClickMate()
    window.show()
    sys.exit(app.exec_())
