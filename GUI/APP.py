import sys
import os

# Get the directory where this script is located (GUI folder)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory (hospital-system folder) where Core and Models are located
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to Python path
sys.path.insert(0, parent_dir)

# Now these imports will work
from Core.hospital import Hospital
from Models.department import Department
from Models.patient import Patient
from Models.staff import Staff

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout, QGridLayout,
    QPushButton, QLabel, QFrame, QLineEdit,
    QTextEdit, QComboBox, QTableWidget, QTableWidgetItem,
    QHeaderView, QMessageBox, QStackedWidget,
    QFormLayout, QSpinBox, QDoubleSpinBox, QScrollArea
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class HospitalGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Initialize hospital system
        self.hospital = Hospital("Smart Hospital")
        
        self.setWindowTitle("Hospital Management System")
        # INCREASED WINDOW SIZE
        self.setMinimumSize(1600, 1000)
        self.resize(1600, 1000)
        
        # Modern color palette
        self.colors = {
            'primary': '#667eea',
            'secondary': '#764ba2',
            'accent1': '#f093fb',
            'accent2': '#4facfe',
            'accent3': '#43e97b',
            'accent4': '#fa709a',
            'sidebar': '#2c3e50',
            'card': '#ffffff',
            'bg': '#f0f4f8',
            'text': '#2d3748',
            'text_light': '#718096',
            'success': '#48bb78',
            'warning': '#ecc94b',
            'danger': '#f56565'
        }
        
        main_widget = QWidget()
        main_layout = QHBoxLayout()
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Sidebar
        sidebar = self.create_sidebar()
        main_layout.addWidget(sidebar)
        
        # Main Content Area with Stack
        self.content_stack = QStackedWidget()
        self.content_stack.setStyleSheet(f"background-color: {self.colors['bg']};")
        
        # Create different pages with scroll areas
        self.dashboard_page = self.create_dashboard_page()
        self.departments_page = self.create_departments_page()
        self.patients_page = self.create_patients_page()
        self.staff_page = self.create_staff_page()
        
        self.content_stack.addWidget(self.dashboard_page)
        self.content_stack.addWidget(self.departments_page)
        self.content_stack.addWidget(self.patients_page)
        self.content_stack.addWidget(self.staff_page)
        
        main_layout.addWidget(self.content_stack, 1)
        
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
        
        # Set global font
        font = QFont("Segoe UI", 10)
        self.setFont(font)
    
    def create_sidebar(self):
        sidebar = QWidget()
        sidebar.setFixedWidth(280)
        sidebar.setStyleSheet(f"""
            QWidget {{
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 {self.colors['sidebar']},
                    stop:1 #1a252f);
            }}
        """)
        
        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(25, 35, 25, 35)
        
        # Logo
        logo_container = QWidget()
        logo_layout = QHBoxLayout()
        logo_layout.setSpacing(15)
        
        logo_icon = QLabel("🏥")
        logo_icon.setStyleSheet("font-size: 36px; background: transparent;")
        
        logo_text = QLabel("MediCare\nPro")
        logo_text.setStyleSheet("""
            color: white;
            font-size: 22px;
            font-weight: bold;
            background: transparent;
        """)
        
        logo_layout.addWidget(logo_icon)
        logo_layout.addWidget(logo_text)
        logo_layout.addStretch()
        logo_container.setLayout(logo_layout)
        logo_container.setStyleSheet("background: transparent;")
        
        layout.addWidget(logo_container)
        layout.addSpacing(40)
        
        # Navigation buttons
        nav_items = [
            ("📊", "Dashboard", 0, self.colors['accent2']),
            ("🏢", "Departments", 1, self.colors['accent3']),
            ("🤒", "Patients", 2, self.colors['accent4']),
            ("👨‍⚕️", "Staff", 3, self.colors['accent1'])
        ]
        
        self.nav_buttons = []
        for icon, text, index, color in nav_items:
            btn = QPushButton(f"{icon}  {text}")
            btn.setStyleSheet(f"""
                QPushButton {{
                    color: white;
                    font-size: 16px;
                    text-align: left;
                    padding: 16px 24px;
                    border-radius: 12px;
                    background-color: transparent;
                    border-left: 4px solid transparent;
                    font-weight: 500;
                }}
                QPushButton:hover {{
                    background-color: rgba(255,255,255,0.1);
                    border-left: 4px solid {color};
                }}
                QPushButton:checked {{
                    background-color: rgba(255,255,255,0.15);
                    border-left: 4px solid {color};
                }}
            """)
            btn.setCursor(Qt.PointingHandCursor)
            btn.setCheckable(True)
            btn.clicked.connect(lambda checked, idx=index: self.switch_page(idx))
            layout.addWidget(btn)
            self.nav_buttons.append(btn)
        
        # Set first button as checked
        self.nav_buttons[0].setChecked(True)
        
        layout.addStretch()
        
        # Hospital Info Card
        info_card = QWidget()
        info_card.setStyleSheet(f"""
            background-color: rgba(255,255,255,0.1);
            border-radius: 16px;
            padding: 20px;
        """)
        info_layout = QVBoxLayout()
        
        info_title = QLabel("🏥 System Status")
        info_title.setStyleSheet("color: white; font-weight: bold; font-size: 14px;")
        
        self.sidebar_depts = QLabel("Departments: 0")
        self.sidebar_depts.setStyleSheet("color: #a0aec0; font-size: 12px;")
        
        self.sidebar_patients = QLabel("Patients: 0")
        self.sidebar_patients.setStyleSheet("color: #a0aec0; font-size: 12px;")
        
        self.sidebar_staff = QLabel("Staff: 0")
        self.sidebar_staff.setStyleSheet("color: #a0aec0; font-size: 12px;")
        
        info_layout.addWidget(info_title)
        info_layout.addWidget(self.sidebar_depts)
        info_layout.addWidget(self.sidebar_patients)
        info_layout.addWidget(self.sidebar_staff)
        info_card.setLayout(info_layout)
        
        layout.addWidget(info_card)
        sidebar.setLayout(layout)
        return sidebar
    
    def switch_page(self, index):
        self.content_stack.setCurrentIndex(index)
        for i, btn in enumerate(self.nav_buttons):
            btn.setChecked(i == index)
        self.update_stats()
    
    def create_dashboard_page(self):
        # Create scroll area for dashboard
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("background-color: transparent; border: none;")
        
        page = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(25)
        layout.setContentsMargins(30, 30, 30, 30)
        
        # Header
        header = QWidget()
        header.setStyleSheet(f"""
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 {self.colors['primary']},
                stop:1 {self.colors['secondary']});
            border-radius: 20px;
        """)
        header.setFixedHeight(160)
        header_layout = QHBoxLayout()
        
        header_text = QVBoxLayout()
        welcome = QLabel("Welcome back, Administrator! 👋")
        welcome.setStyleSheet("color: white; font-size: 32px; font-weight: bold;")
        
        subtitle = QLabel("Hospital Management Dashboard")
        subtitle.setStyleSheet("color: rgba(255,255,255,0.9); font-size: 16px; margin-top: 8px;")
        
        header_text.addWidget(welcome)
        header_text.addWidget(subtitle)
        header_layout.addLayout(header_text)
        header_layout.addStretch()
        
        # Quick action buttons in header
        actions_layout = QHBoxLayout()
        actions_layout.setSpacing(15)
        
        for icon, text, color, callback in [
            ("➕", "Add Dept", self.colors['accent3'], self.quick_add_dept),
            ("👤", "Add Patient", self.colors['accent4'], self.quick_add_patient),
            ("👨‍⚕️", "Add Staff", self.colors['accent1'], self.quick_add_staff)
        ]:
            btn = QPushButton(f"{icon} {text}")
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {color};
                    color: white;
                    border-radius: 10px;
                    padding: 12px 20px;
                    font-weight: bold;
                    font-size: 13px;
                }}
                QPushButton:hover {{
                    background-color: {color}dd;
                }}
            """)
            btn.clicked.connect(callback)
            actions_layout.addWidget(btn)
        
        header_layout.addLayout(actions_layout)
        header.setLayout(header_layout)
        layout.addWidget(header)
        
        # Stats Cards
        cards_grid = QGridLayout()
        cards_grid.setSpacing(20)
        
        self.stat_cards = []
        card_data = [
            ("🏢", "Total Departments", "0", "Active units", self.colors['accent3']),
            ("🤒", "Total Patients", "0", "Admitted", self.colors['accent4']),
            ("👨‍⚕️", "Total Staff", "0", "Employees", self.colors['accent1']),
            ("💰", "Hospital Status", "Active", "Operational", self.colors['accent2'])
        ]
        
        for i, (icon, title, value, subtitle, color) in enumerate(card_data):
            card = self.create_stat_card(icon, title, value, subtitle, color)
            cards_grid.addWidget(card, i // 2, i % 2)
            self.stat_cards.append((card, title))
        
        layout.addLayout(cards_grid)
        
        # Recent Activity
        activity_widget = QWidget()
        activity_widget.setStyleSheet(f"""
            background-color: {self.colors['card']};
            border-radius: 20px;
        """)
        activity_layout = QVBoxLayout()
        activity_layout.setSpacing(15)
        activity_layout.setContentsMargins(30, 30, 30, 30)
        
        activity_header = QLabel("📋 Recent Activity")
        activity_header.setStyleSheet(f"""
            color: {self.colors['text']};
            font-size: 20px;
            font-weight: bold;
        """)
        activity_layout.addWidget(activity_header)
        
        self.activity_list = QVBoxLayout()
        self.activity_list.setSpacing(10)
        
        # Default message
        self.no_activity = QLabel("No recent activity. Start by adding departments, patients, or staff.")
        self.no_activity.setStyleSheet(f"color: {self.colors['text_light']}; font-size: 14px; padding: 20px;")
        self.no_activity.setAlignment(Qt.AlignCenter)
        self.activity_list.addWidget(self.no_activity)
        
        activity_layout.addLayout(self.activity_list)
        activity_layout.addStretch()
        activity_widget.setLayout(activity_layout)
        layout.addWidget(activity_widget, 1)
        
        page.setLayout(layout)
        scroll.setWidget(page)
        return scroll
    
    def create_departments_page(self):
        # Create scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("background-color: transparent; border: none;")
        
        page = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(25)
        layout.setContentsMargins(30, 30, 30, 30)
        
        # Page Header
        header = self.create_page_header("🏢 Department Management", "Manage hospital departments")
        layout.addWidget(header)
        
        # Add Department Form
        form_card = QWidget()
        form_card.setStyleSheet(f"""
            background-color: {self.colors['card']};
            border-radius: 16px;
        """)
        form_layout = QVBoxLayout()
        form_layout.setContentsMargins(25, 25, 25, 25)
        
        form_title = QLabel("Add New Department")
        form_title.setStyleSheet(f"color: {self.colors['text']}; font-size: 18px; font-weight: bold;")
        form_layout.addWidget(form_title)
        
        input_layout = QHBoxLayout()
        
        self.dept_name_input = QLineEdit()
        self.dept_name_input.setPlaceholderText("Enter department name...")
        self.dept_name_input.setStyleSheet(f"""
            QLineEdit {{
                padding: 14px;
                border: 2px solid #e2e8f0;
                border-radius: 10px;
                font-size: 14px;
                background-color: {self.colors['bg']};
            }}
            QLineEdit:focus {{
                border: 2px solid {self.colors['primary']};
            }}
        """)
        
        add_btn = QPushButton("➕ Add Department")
        add_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {self.colors['accent3']};
                color: white;
                padding: 14px 28px;
                border-radius: 10px;
                font-weight: bold;
                font-size: 14px;
            }}
            QPushButton:hover {{
                background-color: {self.colors['accent3']}dd;
            }}
        """)
        add_btn.clicked.connect(self.add_department)
        
        input_layout.addWidget(self.dept_name_input, 1)
        input_layout.addWidget(add_btn)
        
        form_layout.addLayout(input_layout)
        form_card.setLayout(form_layout)
        layout.addWidget(form_card)
        
        # Departments Table - INCREASED HEIGHT
        table_card = QWidget()
        table_card.setStyleSheet(f"""
            background-color: {self.colors['card']};
            border-radius: 16px;
        """)
        table_layout = QVBoxLayout()
        table_layout.setContentsMargins(25, 25, 25, 25)
        
        table_title = QLabel("Departments List")
        table_title.setStyleSheet(f"color: {self.colors['text']}; font-size: 18px; font-weight: bold;")
        table_layout.addWidget(table_title)
        
        self.dept_table = QTableWidget()
        self.dept_table.setColumnCount(4)
        self.dept_table.setHorizontalHeaderLabels(["Name", "Patients", "Staff", "Actions"])
        self.dept_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # INCREASED TABLE HEIGHT
        self.dept_table.setMinimumHeight(400)
        self.dept_table.setStyleSheet(f"""
            QTableWidget {{
                border: none;
                background-color: transparent;
                gridline-color: #e2e8f0;
            }}
            QHeaderView::section {{
                background-color: {self.colors['bg']};
                padding: 12px;
                border: none;
                font-weight: bold;
                color: {self.colors['text']};
            }}
            QTableWidget::item {{
                padding: 12px;
                border-bottom: 1px solid #e2e8f0;
            }}
        """)
        self.dept_table.verticalHeader().setVisible(False)
        
        table_layout.addWidget(self.dept_table)
        table_card.setLayout(table_layout)
        layout.addWidget(table_card, 1)
        
        page.setLayout(layout)
        scroll.setWidget(page)
        return scroll
    
    def create_patients_page(self):
        # Create scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("background-color: transparent; border: none;")
        
        page = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(25)
        layout.setContentsMargins(30, 30, 30, 30)
        
        # Page Header
        header = self.create_page_header("🤒 Patient Management", "Manage patients and medical records")
        layout.addWidget(header)
        
        # Form Card
        form_card = QWidget()
        form_card.setStyleSheet(f"""
            background-color: {self.colors['card']};
            border-radius: 16px;
        """)
        form_layout = QFormLayout()
        form_layout.setContentsMargins(25, 25, 25, 25)
        form_layout.setSpacing(15)
        
        form_title = QLabel("Add New Patient")
        form_title.setStyleSheet(f"color: {self.colors['text']}; font-size: 18px; font-weight: bold;")
        form_layout.addRow(form_title)
        
        # Department selector
        self.patient_dept_combo = QComboBox()
        self.patient_dept_combo.setStyleSheet(f"""
            QComboBox {{
                padding: 12px;
                border: 2px solid #e2e8f0;
                border-radius: 10px;
                background-color: {self.colors['bg']};
                min-width: 200px;
            }}
            QComboBox:focus {{
                border: 2px solid {self.colors['primary']};
            }}
        """)
        form_layout.addRow("Department:", self.patient_dept_combo)
        
        # Name input
        self.patient_name_input = QLineEdit()
        self.patient_name_input.setPlaceholderText("Patient full name")
        self.patient_name_input.setStyleSheet(f"""
            QLineEdit {{
                padding: 12px;
                border: 2px solid #e2e8f0;
                border-radius: 10px;
                background-color: {self.colors['bg']};
            }}
            QLineEdit:focus {{
                border: 2px solid {self.colors['primary']};
            }}
        """)
        form_layout.addRow("Name:", self.patient_name_input)
        
        # Age input
        self.patient_age_input = QSpinBox()
        self.patient_age_input.setRange(0, 120)
        self.patient_age_input.setValue(25)
        self.patient_age_input.setStyleSheet(f"""
            QSpinBox {{
                padding: 12px;
                border: 2px solid #e2e8f0;
                border-radius: 10px;
                background-color: {self.colors['bg']};
            }}
        """)
        form_layout.addRow("Age:", self.patient_age_input)
        
        # Medical record
        self.patient_record_input = QTextEdit()
        self.patient_record_input.setPlaceholderText("Enter medical history and current condition...")
        self.patient_record_input.setMaximumHeight(100)
        self.patient_record_input.setStyleSheet(f"""
            QTextEdit {{
                padding: 12px;
                border: 2px solid #e2e8f0;
                border-radius: 10px;
                background-color: {self.colors['bg']};
                font-family: 'Segoe UI';
            }}
            QTextEdit:focus {{
                border: 2px solid {self.colors['primary']};
            }}
        """)
        form_layout.addRow("Medical Record:", self.patient_record_input)
        
        # Add button
        add_btn = QPushButton("➕ Add Patient")
        add_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {self.colors['accent4']};
                color: white;
                padding: 14px;
                border-radius: 10px;
                font-weight: bold;
                font-size: 14px;
                margin-top: 10px;
            }}
            QPushButton:hover {{
                background-color: {self.colors['accent4']}dd;
            }}
        """)
        add_btn.clicked.connect(self.add_patient)
        form_layout.addRow(add_btn)
        
        form_card.setLayout(form_layout)
        layout.addWidget(form_card)
        
        # Patients Table - INCREASED HEIGHT
        table_card = QWidget()
        table_card.setStyleSheet(f"""
            background-color: {self.colors['card']};
            border-radius: 16px;
        """)
        table_layout = QVBoxLayout()
        table_layout.setContentsMargins(25, 25, 25, 25)
        
        table_title = QLabel("Patients List")
        table_title.setStyleSheet(f"color: {self.colors['text']}; font-size: 18px; font-weight: bold;")
        table_layout.addWidget(table_title)
        
        self.patient_table = QTableWidget()
        self.patient_table.setColumnCount(5)
        self.patient_table.setHorizontalHeaderLabels(["ID", "Name", "Age", "Department", "Medical Record"])
        self.patient_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # INCREASED TABLE HEIGHT
        self.patient_table.setMinimumHeight(400)
        self.patient_table.setStyleSheet(f"""
            QTableWidget {{
                border: none;
                background-color: transparent;
            }}
            QHeaderView::section {{
                background-color: {self.colors['bg']};
                padding: 12px;
                border: none;
                font-weight: bold;
                color: {self.colors['text']};
            }}
            QTableWidget::item {{
                padding: 12px;
                border-bottom: 1px solid #e2e8f0;
            }}
        """)
        self.patient_table.verticalHeader().setVisible(False)
        
        table_layout.addWidget(self.patient_table)
        table_card.setLayout(table_layout)
        layout.addWidget(table_card, 1)
        
        page.setLayout(layout)
        scroll.setWidget(page)
        return scroll
    
    def create_staff_page(self):
        # Create scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("background-color: transparent; border: none;")
        
        page = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(25)
        layout.setContentsMargins(30, 30, 30, 30)
        
        # Page Header
        header = self.create_page_header("👨‍⚕️ Staff Management", "Manage hospital staff and employees")
        layout.addWidget(header)
        
        # Form Card
        form_card = QWidget()
        form_card.setStyleSheet(f"""
            background-color: {self.colors['card']};
            border-radius: 16px;
        """)
        form_layout = QFormLayout()
        form_layout.setContentsMargins(25, 25, 25, 25)
        form_layout.setSpacing(15)
        
        form_title = QLabel("Add New Staff Member")
        form_title.setStyleSheet(f"color: {self.colors['text']}; font-size: 18px; font-weight: bold;")
        form_layout.addRow(form_title)
        
        # Department selector
        self.staff_dept_combo = QComboBox()
        self.staff_dept_combo.setStyleSheet(f"""
            QComboBox {{
                padding: 12px;
                border: 2px solid #e2e8f0;
                border-radius: 10px;
                background-color: {self.colors['bg']};
                min-width: 200px;
            }}
        """)
        form_layout.addRow("Department:", self.staff_dept_combo)
        
        # Name input
        self.staff_name_input = QLineEdit()
        self.staff_name_input.setPlaceholderText("Staff full name")
        self.staff_name_input.setStyleSheet(f"""
            QLineEdit {{
                padding: 12px;
                border: 2px solid #e2e8f0;
                border-radius: 10px;
                background-color: {self.colors['bg']};
            }}
        """)
        form_layout.addRow("Name:", self.staff_name_input)
        
        # Age input
        self.staff_age_input = QSpinBox()
        self.staff_age_input.setRange(18, 80)
        self.staff_age_input.setValue(30)
        self.staff_age_input.setStyleSheet(f"""
            QSpinBox {{
                padding: 12px;
                border: 2px solid #e2e8f0;
                border-radius: 10px;
                background-color: {self.colors['bg']};
            }}
        """)
        form_layout.addRow("Age:", self.staff_age_input)
        
        # Role input
        self.staff_role_input = QLineEdit()
        self.staff_role_input.setPlaceholderText("e.g., Doctor, Nurse, Admin")
        self.staff_role_input.setStyleSheet(f"""
            QLineEdit {{
                padding: 12px;
                border: 2px solid #e2e8f0;
                border-radius: 10px;
                background-color: {self.colors['bg']};
            }}
        """)
        form_layout.addRow("Role:", self.staff_role_input)
        
        # Salary input
        self.staff_salary_input = QDoubleSpinBox()
        self.staff_salary_input.setRange(0, 1000000)
        self.staff_salary_input.setValue(50000)
        self.staff_salary_input.setPrefix("$ ")
        self.staff_salary_input.setStyleSheet(f"""
            QDoubleSpinBox {{
                padding: 12px;
                border: 2px solid #e2e8f0;
                border-radius: 10px;
                background-color: {self.colors['bg']};
            }}
        """)
        form_layout.addRow("Salary:", self.staff_salary_input)
        
        # Add button
        add_btn = QPushButton("➕ Add Staff Member")
        add_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {self.colors['accent1']};
                color: white;
                padding: 14px;
                border-radius: 10px;
                font-weight: bold;
                font-size: 14px;
                margin-top: 10px;
            }}
            QPushButton:hover {{
                background-color: {self.colors['accent1']}dd;
            }}
        """)
        add_btn.clicked.connect(self.add_staff)
        form_layout.addRow(add_btn)
        
        form_card.setLayout(form_layout)
        layout.addWidget(form_card)
        
        # Staff Table - INCREASED HEIGHT
        table_card = QWidget()
        table_card.setStyleSheet(f"""
            background-color: {self.colors['card']};
            border-radius: 16px;
        """)
        table_layout = QVBoxLayout()
        table_layout.setContentsMargins(25, 25, 25, 25)
        
        table_title = QLabel("Staff List")
        table_title.setStyleSheet(f"color: {self.colors['text']}; font-size: 18px; font-weight: bold;")
        table_layout.addWidget(table_title)
        
        self.staff_table = QTableWidget()
        self.staff_table.setColumnCount(6)
        self.staff_table.setHorizontalHeaderLabels(["ID", "Name", "Age", "Role", "Department", "Salary"])
        self.staff_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # INCREASED TABLE HEIGHT
        self.staff_table.setMinimumHeight(400)
        self.staff_table.setStyleSheet(f"""
            QTableWidget {{
                border: none;
                background-color: transparent;
            }}
            QHeaderView::section {{
                background-color: {self.colors['bg']};
                padding: 12px;
                border: none;
                font-weight: bold;
                color: {self.colors['text']};
            }}
            QTableWidget::item {{
                padding: 12px;
                border-bottom: 1px solid #e2e8f0;
            }}
        """)
        self.staff_table.verticalHeader().setVisible(False)
        
        table_layout.addWidget(self.staff_table)
        table_card.setLayout(table_layout)
        layout.addWidget(table_card, 1)
        
        page.setLayout(layout)
        scroll.setWidget(page)
        return scroll
    
    def create_page_header(self, title, subtitle):
        header = QWidget()
        header.setStyleSheet(f"""
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 {self.colors['primary']},
                stop:1 {self.colors['secondary']});
            border-radius: 16px;
        """)
        header.setFixedHeight(120)
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 20, 30, 20)
        
        title_label = QLabel(title)
        title_label.setStyleSheet("color: white; font-size: 28px; font-weight: bold;")
        
        subtitle_label = QLabel(subtitle)
        subtitle_label.setStyleSheet("color: rgba(255,255,255,0.9); font-size: 14px; margin-top: 5px;")
        
        layout.addWidget(title_label)
        layout.addWidget(subtitle_label)
        layout.addStretch()
        header.setLayout(layout)
        return header
    
    def create_stat_card(self, icon, title, value, subtitle, color):
        card = QFrame()
        card.setStyleSheet(f"""
            QFrame {{
                background-color: {self.colors['card']};
                border-radius: 16px;
                border-left: 5px solid {color};
            }}
        """)
        card.setFixedHeight(140)
        layout = QHBoxLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(25, 20, 25, 20)
        
        # Icon
        icon_container = QWidget()
        icon_container.setFixedSize(60, 60)
        icon_container.setStyleSheet(f"""
            background-color: {color}20;
            border-radius: 30px;
        """)
        icon_layout = QVBoxLayout()
        icon_label = QLabel(icon)
        icon_label.setAlignment(Qt.AlignCenter)
        icon_label.setStyleSheet("font-size: 28px;")
        icon_layout.addWidget(icon_label)
        icon_container.setLayout(icon_layout)
        
        # Text
        text_layout = QVBoxLayout()
        title_label = QLabel(title)
        title_label.setStyleSheet(f"color: {self.colors['text_light']}; font-size: 14px;")
        
        value_label = QLabel(value)
        value_label.setStyleSheet(f"""
            color: {self.colors['text']};
            font-size: 32px;
            font-weight: bold;
        """)
        
        subtitle_label = QLabel(subtitle)
        subtitle_label.setStyleSheet(f"color: {color}; font-size: 12px; font-weight: 500;")
        
        text_layout.addWidget(title_label)
        text_layout.addWidget(value_label)
        text_layout.addWidget(subtitle_label)
        text_layout.addStretch()
        
        layout.addWidget(icon_container)
        layout.addLayout(text_layout, 1)
        card.setLayout(layout)
        return card
    
    def add_activity(self, icon, text, color):
        # Remove "no activity" message if present
        if self.no_activity and self.no_activity.isVisible():
            self.no_activity.hide()
        
        item = QWidget()
        item.setStyleSheet(f"""
            QWidget {{
                background-color: {color}15;
                border-radius: 10px;
                border-left: 3px solid {color};
            }}
        """)
        layout = QHBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(15, 12, 15, 12)
        
        icon_label = QLabel(icon)
        icon_label.setStyleSheet("font-size: 16px;")
        
        text_label = QLabel(text)
        text_label.setStyleSheet(f"color: {self.colors['text']}; font-size: 14px;")
        
        layout.addWidget(icon_label)
        layout.addWidget(text_label, 1)
        item.setLayout(layout)
        
        self.activity_list.insertWidget(0, item)
    
    def update_stats(self):
        summary = self.hospital.get_summary()
        
        # Update sidebar
        self.sidebar_depts.setText(f"Departments: {summary['total_departments']}")
        self.sidebar_patients.setText(f"Patients: {summary['total_patients']}")
        self.sidebar_staff.setText(f"Staff: {summary['total_staff']}")
        
        # Update dashboard cards
        values = [
            str(summary['total_departments']),
            str(summary['total_patients']),
            str(summary['total_staff']),
            "Active"
        ]
        
        for (card, title), value in zip(self.stat_cards, values):
            # Find value label and update it
            for child in card.findChildren(QLabel):
                if child.styleSheet() and "font-size: 32px" in child.styleSheet():
                    child.setText(value)
        
        # Update combo boxes
        depts = list(self.hospital.departments.keys())
        for combo in [self.patient_dept_combo, self.staff_dept_combo]:
            combo.clear()
            combo.addItems(depts)
        
        # Update tables
        self.update_dept_table()
        self.update_patient_table()
        self.update_staff_table()
    
    def update_dept_table(self):
        self.dept_table.setRowCount(len(self.hospital.departments))
        for i, (name, dept) in enumerate(self.hospital.departments.items()):
            self.dept_table.setItem(i, 0, QTableWidgetItem(name))
            self.dept_table.setItem(i, 1, QTableWidgetItem(str(len(dept.patients))))
            self.dept_table.setItem(i, 2, QTableWidgetItem(str(len(dept.staff_members))))
            
            # Action buttons
            action_widget = QWidget()
            action_layout = QHBoxLayout()
            action_layout.setSpacing(5)
            
            view_btn = QPushButton("👁 View")
            view_btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {self.colors['accent2']};
                    color: white;
                    padding: 6px 12px;
                    border-radius: 6px;
                    font-size: 12px;
                }}
            """)
            
            delete_btn = QPushButton("🗑 Delete")
            delete_btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {self.colors['danger']};
                    color: white;
                    padding: 6px 12px;
                    border-radius: 6px;
                    font-size: 12px;
                }}
            """)
            delete_btn.clicked.connect(lambda checked, n=name: self.delete_department(n))
            
            action_layout.addWidget(view_btn)
            action_layout.addWidget(delete_btn)
            action_layout.addStretch()
            action_widget.setLayout(action_layout)
            self.dept_table.setCellWidget(i, 3, action_widget)
    
    def update_patient_table(self):
        all_patients = []
        for dept in self.hospital.departments.values():
            for patient in dept.patients.values():
                all_patients.append((patient, dept.name))
        
        self.patient_table.setRowCount(len(all_patients))
        for i, (patient, dept_name) in enumerate(all_patients):
            self.patient_table.setItem(i, 0, QTableWidgetItem(str(patient.id)))
            self.patient_table.setItem(i, 1, QTableWidgetItem(patient.name))
            self.patient_table.setItem(i, 2, QTableWidgetItem(str(patient.age)))
            self.patient_table.setItem(i, 3, QTableWidgetItem(dept_name))
            self.patient_table.setItem(i, 4, QTableWidgetItem(patient.medical_record[:50] + "..."))
    
    def update_staff_table(self):
        all_staff = []
        for dept in self.hospital.departments.values():
            for staff in dept.staff_members.values():
                all_staff.append((staff, dept.name))
        
        self.staff_table.setRowCount(len(all_staff))
        for i, (staff, dept_name) in enumerate(all_staff):
            self.staff_table.setItem(i, 0, QTableWidgetItem(str(staff.id)))
            self.staff_table.setItem(i, 1, QTableWidgetItem(staff.name))
            self.staff_table.setItem(i, 2, QTableWidgetItem(str(staff.age)))
            self.staff_table.setItem(i, 3, QTableWidgetItem(staff.role))
            self.staff_table.setItem(i, 4, QTableWidgetItem(dept_name))
            self.staff_table.setItem(i, 5, QTableWidgetItem(f"${staff.salary:,.2f}"))
    
    # Action handlers
    def quick_add_dept(self):
        self.switch_page(1)
    
    def quick_add_patient(self):
        self.switch_page(2)
    
    def quick_add_staff(self):
        self.switch_page(3)
    
    def add_department(self):
        name = self.dept_name_input.text().strip()
        if not name:
            QMessageBox.warning(self, "Warning", "Please enter a department name.")
            return
        
        dept = Department(name)
        result = self.hospital.add_department(dept)
        
        if "successfully" in result:
            self.dept_name_input.clear()
            self.add_activity("🏢", f"Department '{name}' added successfully", self.colors['accent3'])
            self.update_stats()
            QMessageBox.information(self, "Success", result)
        else:
            QMessageBox.warning(self, "Error", result)
    
    def delete_department(self, name):
        reply = QMessageBox.question(self, "Confirm", f"Delete department '{name}'?")
        if reply == QMessageBox.Yes:
            result = self.hospital.remove_department(name)
            self.add_activity("🗑", f"Department '{name}' removed", self.colors['danger'])
            self.update_stats()
    
    def add_patient(self):
        dept_name = self.patient_dept_combo.currentText()
        name = self.patient_name_input.text().strip()
        age = self.patient_age_input.value()
        record = self.patient_record_input.toPlainText().strip()
        
        if not all([dept_name, name, record]):
            QMessageBox.warning(self, "Warning", "Please fill all fields.")
            return
        
        dept = self.hospital.get_department(dept_name)
        if not dept:
            QMessageBox.warning(self, "Error", "Department not found.")
            return
        
        patient = Patient(name, age, record)
        result = dept.add_patient(patient)
        
        if "successfully" in result:
            self.patient_name_input.clear()
            self.patient_record_input.clear()
            self.patient_age_input.setValue(25)
            self.add_activity("🤒", f"Patient '{name}' added to {dept_name}", self.colors['accent4'])
            self.update_stats()
            QMessageBox.information(self, "Success", result)
        else:
            QMessageBox.warning(self, "Error", result)
    
    def add_staff(self):
        dept_name = self.staff_dept_combo.currentText()
        name = self.staff_name_input.text().strip()
        age = self.staff_age_input.value()
        role = self.staff_role_input.text().strip()
        salary = self.staff_salary_input.value()
        
        if not all([dept_name, name, role]):
            QMessageBox.warning(self, "Warning", "Please fill all fields.")
            return
        
        dept = self.hospital.get_department(dept_name)
        if not dept:
            QMessageBox.warning(self, "Error", "Department not found.")
            return
        
        staff = Staff(name, age, role, dept_name, salary)
        result = dept.add_staff(staff)
        
        if "successfully" in result:
            self.staff_name_input.clear()
            self.staff_role_input.clear()
            self.staff_age_input.setValue(30)
            self.staff_salary_input.setValue(50000)
            self.add_activity("👨‍⚕️", f"Staff '{name}' ({role}) added to {dept_name}", self.colors['accent1'])
            self.update_stats()
            QMessageBox.information(self, "Success", result)
        else:
            QMessageBox.warning(self, "Error", result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Set application font
    font = QFont("Segoe UI", 10)
    app.setFont(font)
    
    window = HospitalGUI()
    window.show()
    sys.exit(app.exec())