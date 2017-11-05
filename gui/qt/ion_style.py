"""Ion look and feel."""

ion_stylesheet = '''
* {
    font-family: "Source Sans Pro", Candara, Calibri, Verdana, Arial, sans serif;
    font-weight: normal;
    font-size: 10pt;
}

/* Lite Mode -- cloned from "CleanLook" theme */
#main_window {
    /*border-image: url(:/icons/bg.png) 0 0 0 0 stretch stretch;*/
}

MiniWindow QPushButton {
    color: #777;
    /*border: 1px solid #CCC;*/
    border-radius: 0;
    /*background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 white, stop: 1 #E6E6E6);*/
    min-height: 30px;
    min-width: 30px;
    border: none;
}

#send_button{
    background-color: #00adf6;
    color: white;
    /*border: 1px solid #3786E6;*/
    /*border-radius: 4px;*/
    /*background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #72B2F8, stop: 1 #3484E6);*/
    padding: 2px;
    width: 20px;
}

#send_button:disabled{
    color: #D3E8FE;
    /*border: 1px solid #6DAEF7;*/
    /*border-radius: 4px;*/
    /*background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #A5CFFA, stop: 1 #72B2F8);*/
}
#address_input, #amount_input, #label_input
{
    color: #000;
    padding: 5px;
    min-height: 23px;
    width: 200px;
}

QWidget {
    border: 1px solid rgba(204,204,204,0);
    border-radius: 4px;
}

#address_input[isValid=true]
{
    color: #4D9948;
}

#address_input[isValid=false]
{
    color: #CE4141;
}

#balance_label
{
    color: #333;
}

#history
{
    color: #888;
}


/**********************/
/* ION Evolution CSS */
/*
0. OSX Reset
1. Navigation Bar
2. Editable Fields, Labels
3. Containers
4. File Menu, Toolbar
5. Buttons, Spinners, Dropdown
6. Table Headers
7. Scroll Bar
8. Tree View
9. Dialog Boxes
*/
/**********************/


/**********************/
/* 0. OSX Reset */

QWidget { /* Set default style for QWidget, override in following statements */
    border: 0;
}


/**********************/
/* 1. Navigation Bar */

#main_window_nav_bar {
    border:0;
}

#main_window_nav_bar QTabBar {
    color: #fff;
    border:0;
    background: url(':/icons/ion_logo_text.png') no-repeat left center;
    margin-left: 25px;
}

QTabWidget#main_window_nav_bar::tab-bar {
    alignment: left;
}

QTabWidget#main_window_nav_bar::pane {
    /*position: absolute;*/
}

#main_window_nav_bar QTabBar::tab {
    /*background-color:#1e75b4;*/
    color:#fff;
    min-height: 60px;
    padding-left:1em;
    padding-right:1em;
    border-left: 1px solid #595a68;
    border-right: 1px solid #595a68;

}

#main_window_nav_bar QTabBar::tab:first {
    border-left: none;
    margin-left:200px;
}

#main_window_nav_bar QTabBar::tab:last {
    /*border-right: 0 solid #fff;*/
}

#main_window_nav_bar QTabBar::tab:selected, #main_window_nav_bar QTabBar::tab:hover {
    /*background-color:#0d436e;*/
    color:#fff;
}

QStatusBar {
    background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #0C1C24, stop: 1 #3A2C4B);
    border: none;
}

StatusBarButton {
    border: none;
    padding: 0;
    margin: 0;
    outline: 0;
}

QPushButton {
    outline: 0;
}

/**********************/
/* 2. Editable Fields and Labels */

QCheckBox { /* Checkbox Labels */
    color:#333333;
    background-color:transparent;
}

QCheckBox:hover {
    background-color:transparent;
}

QValidatedLineEdit, QLineEdit, PayToEdit { /* Text Entry Fields */
    border: 1px solid rgb(51,51,51,100);
    min-height:25px;
    outline:0;
    padding:3px;
    /*background-color:#fcfcfc;*/
    color: #333;
}

ButtonsLineEdit {
    color: #333;
    min-height:25px;
    background: #fff;
}

QLabel {
    color: #333;
    min-height:25px;
}


/**********************/
/* 3. Containers */


/* Wallet Container */
#main_window_container {
    background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #0C1C24, stop: 1 #3A2C4B);
    color: #fff;
}
#main_window_container QPushButton {
    /* Buttons
    background-color: #00adf6;
    color: white;*/
}

#history_container , #send_container, #receive_container, #contacts_container, #addresses_container, #console_container {
    padding: 20;
    background-color: white;
}

#history_container QPushButton, #send_container QPushButton, #receive_container QPushButton, #contacts_container QPushButton, #addresses_container QPushButton, #console_container QPushButton {
    border: 1px solid #00adf6;
}


/* History Container */
#history_container {
    /*background-color:#FF0000;
    background:qradialgradient(cx:0.5, cy:0.5, radius: 0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop: 1 rgba(246, 246, 246, 255));*/
}


/* Send Container */
#send_container {
    /*background-color:#FF0000;
    background:qradialgradient(cx:0.5, cy:0.5, radius: 0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop: 1 rgba(246, 246, 246, 255));*/
}

#send_container QLabel {
    margin-left:10px;
    min-width:140px;
}


/* Receive Container */
#receive_container {
    /*background-color:#FF0000;
    background:qradialgradient(cx:0.5, cy:0.5, radius: 0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop: 1 rgba(246, 246, 246, 255));*/
}

#receive_container QLabel {
    margin-left:10px;
    min-width:142px;
}


/* Addressses Container */
#addresses_container {
    /*background:qradialgradient(cx:0.5, cy:0.5, radius: 0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop: 1 rgba(246, 246, 246, 255));*/
}


/* Contacts Container */
#contacts_container {
    /*background:qradialgradient(cx:0.5, cy:0.5, radius: 0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop: 1 rgba(233, 233, 233, 255));*/
}


/* Console Container */
#console_container {
}


/* Balance Label */
#main_window_balance {
    color:#ffffff;
    font-weight:bold;
    margin-left:10px;
}


/**********************/
/* 4. File Menu, Toolbar */

#main_window_container QMenuBar {
    color: #fff;
}

QMenuBar {
    background-color:#fff;
}

QMenuBar::item {
    background-color:#fff;
    color:#333;
}

QMenuBar::item:selected {
    /*background-color:#f8f6f6;*/
}

QMenu {
    /*background-color:#f8f6f6;*/
    border:1px solid #2B2727;
}

QMenu::item {
    color:#333;
}

QMenu::item:selected {
    /*background-color:#f2f0f0;*/
    color:#333;
}

QToolBar {
    /*background-color:#3398CC;*/
    border:0px solid #000;
    padding:0;
    margin:0;
}

QToolBar > QToolButton {
    /*background-color:#3398CC;*/
    border:0;
    min-height:2.5em;
    font-weight:bold;
    color:#fff;
}

QToolBar > QToolButton:checked {
    background-color:#fff;
    color:#333;
    font-weight:bold;
}

QMessageBox {
    /*background-color:#F8F6F6;*/
}


QLabel { /* Base Text Size & Color */
    color:#333333;
}


/**********************/
/* 5. Buttons, Spinners, Dropdown */

CancelButton, CloseButton, QPushButton { /* Global Button Style */
    /*background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: .01 #64ACD2, stop: .1 #3398CC, stop: .95 #3398CC, stop: 1 #1D80B5);*/
    border-radius:6px;
    color:#00adf6;
    /* font-size:12px; */
    font-weight:bold;
    padding-left:25px;
    padding-right:25px;
    padding-top:5px;
    padding-bottom:5px;
    min-height:25px;
}

QPushButton:hover {
    /*background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: .01 #64ACD2, stop: .1 #46AADE, stop: .95 #46AADE, stop: 1 #1D80B5);*/
}

QPushButton:focus {
    border:none;
    outline:none;
}

QPushButton:pressed {
    /*border:1px solid #333;*/
    border:none;
    outline:none;
}

QComboBox { /* Dropdown Menus */
    border: 1px solid rgb(51,51,51,100);
    padding: 3px 5px 3px 5px;
    /*background:#fcfcfc;*/
    min-height:25px;
    /*color:#818181;*/
}

QComboBox:checked {
    /*background:#f2f2f2;*/
}

QComboBox:editable {
    /*background: #3398CC;
    color:#616161;*/
    border:0px solid transparent;
}

QComboBox::drop-down {
    width:25px;
    border:0px;
}

QComboBox::down-arrow {
    border-image: url(':/icons/ion_downArrow.png') 0 0 0 0 stretch stretch;
}

QComboBox QListView {
    background:#fff;
    border:1px solid #333;
    padding-right:1px;
    padding-left:1px;
}

QComboBox QAbstractItemView::item { margin:4px; }

QComboBox::item {
    color:#818181;
}

QComboBox::item:alternate {
    background:#fff;
}

QComboBox::item:selected {
    border:0px solid transparent;
    background:#f2f2f2;
}

QComboBox::indicator {
    background-color:transparent;
    selection-background-color:transparent;
    color:transparent;
    selection-color:transparent;
}

QAbstractSpinBox {
    border:1px solid #82C3E6;
    padding: 3px 5px 3px 5px;
    background:#fcfcfc;
    min-height:25px;
    color:#818181;
}

QAbstractSpinBox::up-button {
    subcontrol-origin: border;
    subcontrol-position: top right;
    width:21px;
    background:#fcfcfc;
    border-left:0px;
    border-right:1px solid #82C3E6;
    border-top:1px solid #82C3E6;
    border-bottom:0px;
    padding-right:1px;
    padding-left:5px;
    padding-top:2px;
}


QAbstractSpinBox::down-button {
    subcontrol-origin: border;
    subcontrol-position: bottom right;
    width:21px;
    background:#fcfcfc;
    border-top:0px;
    border-left:0px;
    border-right:1px solid #82C3E6;
    border-bottom:1px solid #82C3E6;
    padding-right:1px;
    padding-left:5px;
    padding-bottom:2px;
}


/**********************/
/* 6. Table Headers */

QHeaderView { /* Table Header */
    border:0px;
    background-color:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #022844, stop: 1 #0363A5);
}

/* Headings above tree */
QHeaderView::section { /* Table Header Sections */
    qproperty-alignment:left;
    color:#fff;
    min-width: 50px;
    min-height:25px;
    font-weight:bold;
    font-size:11px;
    outline:0;
    border:0;
    border-right:1px solid #56ABD8;
    padding-left:10px;
    padding-right:10px;
    padding-top:1px;
    padding-bottom:1px;
    background-color: transparent;
}

#contacts_container QHeaderView::section {
}

#contacts_container QHeaderView::section:first {
    padding-left:50px;
    padding-right:40px;
}

QHeaderView::section:last {
    border-right: 0px solid #d7d7d7;
}


/**********************/
/* 7. Scroll Bar */

QScrollBar { /* Scroll Bar */

}

QScrollBar:vertical { /* Vertical Scroll Bar Attributes */
    border:0;
    background:#ffffff;
    width:18px;
    margin: 18px 0px 18px 0px;
}

QScrollBar:horizontal { /* Horizontal Scroll Bar Attributes */
    border:0;
    background:#ffffff;
    height:18px;
    margin: 0px 18px 0px 18px;
}


QScrollBar::handle:vertical { /* Scroll Bar Slider - vertical */
    background:#e0e0e0;
    min-height:10px;
}

QScrollBar::handle:horizontal { /* Scroll Bar Slider - horizontal */
    /*background:#e0e0e0;*/
    min-width:10px;
}

QScrollBar::add-page, QScrollBar::sub-page { /* Scroll Bar Background */
    /*background:#F8F6F6;*/
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical, QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal { /* Define Arrow Button Dimensions */
    /*background-color:#F8F6F6;*/
    border: 1px solid #f2f0f0;
    width:16px;
    height:16px;
}

QScrollBar::add-line:vertical:pressed, QScrollBar::sub-line:vertical:pressed, QScrollBar::add-line:horizontal:pressed, QScrollBar::sub-line:horizontal:pressed {
    /*background-color:#e0e0e0;*/
}

QScrollBar::sub-line:vertical { /* Vertical - top button position */
    subcontrol-position:top;
    subcontrol-origin: margin;
}

QScrollBar::add-line:vertical { /* Vertical - bottom button position */
    subcontrol-position:bottom;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal { /* Vertical - left button position */
    subcontrol-position:left;
    subcontrol-origin: margin;
}

QScrollBar::add-line:horizontal { /* Vertical - right button position */
    subcontrol-position:right;
    subcontrol-origin: margin;
}

QScrollBar:up-arrow, QScrollBar:down-arrow, QScrollBar:left-arrow, QScrollBar:right-arrow { /* Arrows Icon */
    width:10px;
    height:10px;
}

QScrollBar:up-arrow {
    background-image: url(':/icons/ion_upArrow_small.png');
}

QScrollBar:down-arrow {
    background-image: url(':/icons/ion_downArrow_small.png');
}

QScrollBar:left-arrow {
    background-image: url(':/icons/ion_leftArrow_small.png');
}

QScrollBar:right-arrow {
    background-image: url(':/icons/ion_rightArrow_small.png');
}


/**********************/
/* 8. Tree Widget */

QTreeWidget {
    border: 0;
    background-color:rgba(255,255,255,128); /* Content view */
}

QTreeWidget::item {
    color:#333;
}

/**********************/
/* 9. Dialog Boxes */

QDialog {
    /*background:qradialgradient(cx:0.5, cy:0.5, radius: 0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop: 1 rgba(233, 233, 233, 255));*/
}

QDialog QTabWidget {
    border-bottom:1px solid #333;
}

QDialog QTabWidget::pane {
    border: 1px solid #d7d7d7;
}

QDialog QTabWidget QTabBar::tab {
    /*background-color:#f2f0f0;*/
    color:#333;
    padding-left:10px;
    padding-right:10px;
    padding-top:5px;
    padding-bottom:5px;
    border-top: 1px solid #d7d7d7;
}

QDialog QTabWidget QTabBar::tab:first {
    border-left: 1px solid #d7d7d7;
}

QDialog QTabWidget QTabBar::tab:last {
    border-right: 1px solid #d7d7d7;
}

QDialog QTabWidget QTabBar::tab:selected, QDialog QTabWidget QTabBar::tab:hover {
    background-color:#ffffff;
    color:#333;
}

QDialog QTabWidget QWidget {
    background-color:#fff;
    color:#333;
}

QDialog QTabWidget QWidget QAbstractSpinBox {
    min-height:15px;
}

QDialog QTabWidget QWidget QAbstractSpinBox::down-button {
    width:15px;
}

QDialog QTabWidget QWidget QAbstractSpinBox::up-button {
    width:15px;
}

QDialog QTabWidget QWidget QComboBox {
    min-height:15px;
}

QDialog QWidget { /* Remove Annoying Focus Rectangle */
    outline: 0;
}

QWidget {
    outline: 0;
}


StatusBarButton {
    border: none !important;
    padding: 0;
    margin: 0;
    outline: none !important;
}
'''