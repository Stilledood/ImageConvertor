from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets,QtCore
import os
from FolderManiipulation import *
from filters import *
from Resize import *




class MainWindow(QMainWindow):

    def __init__(self,parent=None):
        super(MainWindow,self).__init__()
        self.resize(400,300)



    def browse_files(self):
        self.folderpath = QtWidgets.QFileDialog.getExistingDirectory(self)
        if len(self.folderpath) > 0:
            self.run_button.setEnabled(True)





    def SetupUi(self):
        self.button=QPushButton(self)
        self.button.setText('Browse files')
        self.button.setFixedSize(150,30)
        self.button.move(125,200)



        self.button.clicked.connect(self.browse_files)




        self.sub_window=Options_window()
        self.run_button=QPushButton(self)
        self.run_button.setEnabled(False)
        self.run_button.setText("Run")
        self.path = QLineEdit()



        self.run_button.clicked.connect(self.sub_window.show)
        self.sub_window.save_button.clicked.connect(self.run_settings)



    def run_settings(self):
        self.sub_window.save_button.setEnabled(False)
        create_dir(self.folderpath)
        new_path=self.folderpath+'/Resized'
        filter=self.sub_window.filter_menu.currentText()
        resize = ''
        if self.sub_window.medium_box.isChecked():
            resize = 'Medium'
        elif self.sub_window.small_box.isChecked():
            resize = 'Small'

        else:
            resize=self.sub_window.custom_box.text()


        for file in os.listdir(self.folderpath):

            filename=os.fsdecode(file)
            file_path=self.folderpath+'/'+filename


            if filename.endswith('.jpg'):

                if filter == 'B%W':
                    black_white_image=black_and_white(file_path)
                    if resize == 'Medium':
                        final_resized_image=medium_resize(black_white_image)
                        save_file(final_resized_image,filename,new_path)
                    elif resize == 'Small':
                        final_resized_image=small_resize(black_white_image)
                        save_file(final_resized_image,filename,new_path)
                    elif resize != '':
                        try:
                            final_resized_image=custom_resize_by_height(black_white_image,int(resize))
                            save_file(final_resized_image,filename,new_path)
                        except:
                            pass
                    else:
                        save_file(black_white_image,filename,new_path)


                elif filter == 'Sharpen':
                    sharped_image=sharpen(file_path)
                    if resize == 'Medium':
                        final_resized_image=medium_resize(sharped_image)
                        save_file(final_resized_image,filename,new_path)
                    elif resize == 'Small':
                        final_resized_image=small_resize(sharped_image)
                        save_file(final_resized_image,filename,new_path)
                    elif resize != '':
                        try:
                            final_resized_image=custom_resize_by_height(sharped_image,int(resize))
                            save_file(final_resized_image,filename,new_path)
                        except:
                            pass

                    else:
                        save_file(sharped_image,filename,new_path)


                elif filter == 'Increase COntrast':
                    increase_contrast_image=increase_contrast(file_path)
                    if resize == 'Medium':
                        final_resized_image = medium_resize(increase_contrast_image)
                        save_file(final_resized_image, filename, new_path)
                    elif resize == 'Small':
                        final_resized_image = small_resize(increase_contrast_image)
                        save_file(final_resized_image, filename, new_path)
                    elif resize != '':
                        try:
                            final_resized_image = custom_resize_by_height(increase_contrast_image, int(resize))
                            save_file(final_resized_image, filename, new_path)
                        except:
                            pass

                    else:
                        save_file(increase_contrast_image, filename, new_path)


                elif filter == 'Decrease contrast':
                    decreased_contrast_image=decrease_contrast(file_path)
                    if resize == 'Medium':
                        final_resized_image = medium_resize(decreased_contrast_image)
                        save_file(final_resized_image, filename, new_path)
                    elif resize == 'Small':
                        final_resized_image = small_resize(decreased_contrast_image)
                        save_file(final_resized_image, filename, new_path)
                    elif resize != '':
                        try:
                            final_resized_image = custom_resize_by_height(decreased_contrast_image, int(resize))
                            save_file(final_resized_image, filename, new_path)
                        except:
                            pass

                    else:
                        save_file(decreased_contrast_image, filename, new_path)


                elif filter == 'Increase Brightness':
                    increased_bright_image=increase_brightness(file_path)
                    if resize == 'Medium':
                        final_resized_image = medium_resize(increased_bright_image)
                        save_file(final_resized_image, filename, new_path)
                    elif resize == 'Small':
                        final_resized_image = small_resize(increased_bright_image)
                        save_file(final_resized_image, filename, new_path)
                    elif resize != '':
                        try:
                            final_resized_image = custom_resize_by_height(increased_bright_image, int(resize))
                            save_file(final_resized_image, filename, new_path)
                        except:
                            pass

                    else:
                        save_file(increased_bright_image, filename, new_path)


                elif filter == 'Decrease Brightness':
                    decreased_bright_image=decreasse_brightness(file_path)
                    if resize == 'Medium':
                        final_resized_image = medium_resize(decreased_bright_image)
                        save_file(final_resized_image, filename, new_path)
                    elif resize == 'Small':
                        final_resized_image = small_resize(decreased_bright_image)
                        save_file(final_resized_image, filename, new_path)
                    elif resize != '':
                        try:
                            final_resized_image = custom_resize_by_height(decreased_bright_image, int(resize))
                            save_file(final_resized_image, filename, new_path)
                        except:
                            pass

                    else:
                        save_file(decreased_bright_image, filename, new_path)


                elif filter == 'None':
                    image=Image.open(file_path)
                    if resize == 'Medium':
                        final_resized_image = medium_resize(image)
                        save_file(final_resized_image, filename, new_path)
                    elif resize == 'Small':
                        final_resized_image = small_resize(image)
                        save_file(final_resized_image, filename, new_path)
                    elif resize != '':
                        try:
                            final_resized_image = custom_resize_by_height(image, int(resize))
                            save_file(final_resized_image, filename, new_path)
                        except:
                            pass

                    else:
                        save_file(image, filename, new_path)






class Options_window(QWidget):
    def __init__(self):
        super(Options_window,self).__init__()
        self.resize(800,600)


        self.filter_menu = QComboBox(self)
        filters = ['None', 'B%W', 'Sharpen', 'Increase COntrast', 'Decrease contrast', 'Increase Brightness',
                   'Decrease Brightness']
        self.filter_menu.addItems(filters)
        self.filter_menu.setFixedSize(150, 30)
        self.filter_menu.move(200,200)
        groupbox_filters=QGroupBox('Filters')
        filter_box=QVBoxLayout()
        filter_box.addWidget(self.filter_menu)
        groupbox_filters.setLayout(filter_box)


        self.medium_box = QCheckBox(self)
        self.medium_box.setText('Medium')
        self.medium_box.move(100,150)

        self.small_box = QCheckBox(self)
        self.small_box.setText('Small')
        self.small_box.move(100, 200)

        self.custom_box = QLineEdit(self)
        self.label_custom=QLabel(self)
        self.label_custom.setText('Custom Height')
        self.label_custom.move(40,15)
        self.custom_box.resize(30, 15)
        self.custom_box.move(200, 100)

        box_resize=QGroupBox('Resize')
        resize_box=QVBoxLayout()
        resize_box.addWidget(self.medium_box)
        resize_box.addWidget(self.small_box)
        resize_box.addWidget(self.custom_box)
        resize_box.addWidget(self.label_custom)
        box_resize.setLayout(resize_box)

        self.save_as = QComboBox(self)
        save_items = ['jpeg', 'png']
        self.save_as.addItems(save_items)
        self.save_as.setFixedSize(150, 30)
        self.save_as.move(150,100)
        group_box_save=QGroupBox('Save As')
        save_box=QVBoxLayout()
        save_box.addWidget(self.save_as)
        group_box_save.setLayout(save_box)

        self.save_button = QPushButton(self)
        self.save_button.setText('Save')
        self.save_button.setFixedSize(100, 30)
        self.save_button.move(200,200)
        save_button_box=QGroupBox("Save")
        save_button=QVBoxLayout()
        save_button.addWidget(self.save_button)
        save_button_box.setLayout(save_button)





        grid=QGridLayout()
        grid.addWidget(groupbox_filters,0,0)
        grid.addWidget(group_box_save,1,0)
        grid.addWidget(box_resize,0,1)
        grid.addWidget(save_button_box,1,1)
        self.setLayout(grid)

































if __name__=='__main__':
    app=QApplication(sys.argv)
    app.setStyle('Fusion')

    window=MainWindow()

    window.SetupUi()
    window.show()
    sys.exit(app.exec())


