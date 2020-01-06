# -*- coding: ISO-8859-1 -*-
#
# generated by wxGlade 0.9.3 on Thu Jun 27 21:45:40 2019
#

import wx
from icons import icons8_administrative_tools_50
_ = wx.GetTranslation

# begin wxGlade: dependencies
# end wxGlade


class Preferences(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Preferences.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE | wx.FRAME_TOOL_WINDOW | wx.STAY_ON_TOP
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((381, 523))
        self.combobox_board = wx.ComboBox(self, wx.ID_ANY, choices=["M2", "B2", "M", "M1", "A", "B", "B1"], style=wx.CB_DROPDOWN)
        self.checkbox_1 = wx.CheckBox(self, wx.ID_ANY, _("Flip X"))
        self.checkbox_3 = wx.CheckBox(self, wx.ID_ANY, _("Home Right"))
        self.checkbox_2 = wx.CheckBox(self, wx.ID_ANY, _("Flip Y"))
        self.checkbox_4 = wx.CheckBox(self, wx.ID_ANY, _("Home Bottom"))
        self.spin_speed_max = wx.SpinCtrl(self, wx.ID_ANY, "240", min=0, max=1000)
        self.spin_speed_max_raster = wx.SpinCtrl(self, wx.ID_ANY, "480", min=0, max=1000)
        self.spin_home_x = wx.SpinCtrlDouble(self, wx.ID_ANY, "0.0", min=-50000.0, max=50000.0)
        self.spin_home_y = wx.SpinCtrlDouble(self, wx.ID_ANY, "0.0", min=-50000.0, max=50000.0)
        self.button_home_by_current = wx.Button(self, wx.ID_ANY, _("Set Current"))
        self.radio_units = wx.RadioBox(self, wx.ID_ANY, _("Units"), choices=[_("mm"), _("cm"), _("inch"), _("mils")], majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        self.spin_bedwidth = wx.SpinCtrlDouble(self, wx.ID_ANY, "330.0", min=1.0, max=1000.0)
        self.spin_bedheight = wx.SpinCtrlDouble(self, wx.ID_ANY, "230.0", min=1.0, max=1000.0)
        self.checkbox_autolock = wx.CheckBox(self, wx.ID_ANY, _("Automatically lock rail"))
        self.checkbox_autohome = wx.CheckBox(self, wx.ID_ANY, _("Home after job complete"))
        self.checkbox_autobeep = wx.CheckBox(self, wx.ID_ANY, _("Beep after job complete"))
        self.checkbox_mock_usb = wx.CheckBox(self, wx.ID_ANY, _("Mock USB Connection Mode"))
        self.checkbox_multiple_devices = wx.CheckBox(self, wx.ID_ANY, _("Multiple Devices"))
        self.spin_device_index = wx.SpinCtrl(self, wx.ID_ANY, "-1", min=-1, max=5)
        self.spin_device_address = wx.SpinCtrl(self, wx.ID_ANY, "-1", min=-1, max=5)
        self.spin_device_bus = wx.SpinCtrl(self, wx.ID_ANY, "-1", min=-1, max=5)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_COMBOBOX, self.on_combobox_boardtype, self.combobox_board)
        self.Bind(wx.EVT_CHECKBOX, self.on_check_flip_x, self.checkbox_1)
        self.Bind(wx.EVT_CHECKBOX, self.on_check_home_right, self.checkbox_3)
        self.Bind(wx.EVT_CHECKBOX, self.on_check_flip_y, self.checkbox_2)
        self.Bind(wx.EVT_CHECKBOX, self.on_check_home_bottom, self.checkbox_4)
        self.Bind(wx.EVT_SPINCTRL, self.spin_on_speed_vector_max, self.spin_speed_max)
        self.Bind(wx.EVT_TEXT_ENTER, self.spin_on_speed_vector_max, self.spin_speed_max)
        self.Bind(wx.EVT_SPINCTRL, self.spin_on_speed_raster_max, self.spin_speed_max_raster)
        self.Bind(wx.EVT_TEXT_ENTER, self.spin_on_speed_raster_max, self.spin_speed_max_raster)
        self.Bind(wx.EVT_SPINCTRLDOUBLE, self.spin_on_home_x, self.spin_home_x)
        self.Bind(wx.EVT_TEXT_ENTER, self.spin_on_home_x, self.spin_home_x)
        self.Bind(wx.EVT_SPINCTRLDOUBLE, self.spin_on_home_y, self.spin_home_y)
        self.Bind(wx.EVT_TEXT_ENTER, self.spin_on_home_y, self.spin_home_y)
        self.Bind(wx.EVT_BUTTON, self.on_button_set_home_current, self.button_home_by_current)
        self.Bind(wx.EVT_RADIOBOX, self.on_radio_units, self.radio_units)
        self.Bind(wx.EVT_SPINCTRLDOUBLE, self.spin_on_bedwidth, self.spin_bedwidth)
        self.Bind(wx.EVT_SPINCTRLDOUBLE, self.spin_on_bedheight, self.spin_bedheight)
        self.Bind(wx.EVT_CHECKBOX, self.on_check_autolock, self.checkbox_autolock)
        self.Bind(wx.EVT_CHECKBOX, self.on_check_autohome, self.checkbox_autohome)
        self.Bind(wx.EVT_CHECKBOX, self.on_check_autobeep, self.checkbox_autobeep)
        self.Bind(wx.EVT_CHECKBOX, self.on_checkbox_mock_usb, self.checkbox_mock_usb)
        self.Bind(wx.EVT_CHECKBOX, self.on_checkbox_multiple_devices, self.checkbox_multiple_devices)
        self.Bind(wx.EVT_SPINCTRL, self.spin_on_device_index, self.spin_device_index)
        self.Bind(wx.EVT_TEXT_ENTER, self.spin_on_device_index, self.spin_device_index)
        self.Bind(wx.EVT_SPINCTRL, self.spin_on_device_address, self.spin_device_address)
        self.Bind(wx.EVT_TEXT_ENTER, self.spin_on_device_address, self.spin_device_address)
        self.Bind(wx.EVT_SPINCTRL, self.spin_on_device_bus, self.spin_device_bus)
        self.Bind(wx.EVT_TEXT_ENTER, self.spin_on_device_bus, self.spin_device_bus)

        # end wxGlade
        self.project = None
        self.Bind(wx.EVT_CLOSE, self.on_close, self)

    def on_close(self, event):
        try:
            del self.project.windows["preferences"]
        except KeyError:
            pass
        event.Skip()  # Call destroy.

    def set_project(self, project):
        self.project = project
        self.checkbox_mock_usb.SetValue(self.project.controller.mock)
        self.checkbox_autobeep.SetValue(self.project.autobeep)
        self.checkbox_autohome.SetValue(self.project.autohome)
        self.checkbox_autolock.SetValue(self.project.writer.autolock)
        self.combobox_board.SetValue(self.project.writer.board)
        self.spin_bedwidth.SetValue(self.project.size[0])
        self.spin_bedheight.SetValue(self.project.size[1])
        self.radio_units.SetSelection(self.project.units[3])
        self.spin_device_index.SetValue(self.project.controller.usb_index)
        self.spin_device_bus.SetValue(self.project.controller.usb_bus)
        self.spin_device_address.SetValue(self.project.controller.usb_address)
        self.checkbox_multiple_devices.SetValue(self.spin_device_index.GetValue() != -1 or
                                                self.spin_device_bus.GetValue() != -1 or
                                                self.spin_device_address.GetValue() != -1)
        self.on_checkbox_multiple_devices(None)

    def __set_properties(self):
        # begin wxGlade: Preferences.__set_properties
        self.SetTitle(_("Preferences"))
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(icons8_administrative_tools_50.GetBitmap())
        self.SetIcon(_icon)
        self.combobox_board.SetToolTip(_("Select the board to use. This has an effects the speedcodes used."))
        self.combobox_board.SetSelection(0)
        self.checkbox_1.SetToolTip(_("Flip the Right and Left commands sent to the controller"))
        self.checkbox_1.Enable(False)
        self.checkbox_3.SetToolTip(_("Indicates the device Home is on the right"))
        self.checkbox_3.Enable(False)
        self.checkbox_2.SetToolTip(_("Flip the Top and Bottom commands sent to the controller"))
        self.checkbox_2.Enable(False)
        self.checkbox_4.SetToolTip(_("Indicates the device Home is on the bottom"))
        self.checkbox_4.Enable(False)
        self.spin_speed_max.SetMinSize((94, 23))
        self.spin_speed_max.SetToolTip(_("Speedcode permitted maximum set for vectors"))
        self.spin_speed_max.Enable(False)
        self.spin_speed_max_raster.SetMinSize((94, 23))
        self.spin_speed_max_raster.SetToolTip(_("Speedcode permitted maximum set for rasters"))
        self.spin_speed_max_raster.Enable(False)
        self.spin_home_x.SetMinSize((80, 23))
        self.spin_home_x.SetToolTip(_("Translate Home X"))
        self.spin_home_x.Enable(False)
        self.spin_home_y.SetMinSize((80, 23))
        self.spin_home_y.SetToolTip(_("Translate Home Y"))
        self.spin_home_y.Enable(False)
        self.button_home_by_current.SetToolTip(_("Set Home Position based on the current position"))
        self.button_home_by_current.Enable(False)
        self.radio_units.SetBackgroundColour(wx.Colour(192, 192, 192))
        self.radio_units.SetToolTip(_("Set default units for guides"))
        self.radio_units.SetSelection(0)
        self.spin_bedwidth.SetMinSize((80, 23))
        self.spin_bedwidth.SetToolTip(_("Width of the laser bed."))
        self.spin_bedheight.SetMinSize((80, 23))
        self.spin_bedheight.SetToolTip(_("Height of the laser bed."))
        self.checkbox_autolock.SetToolTip(_("Lock rail after operations are finished."))
        self.checkbox_autolock.SetValue(1)
        self.checkbox_autohome.SetToolTip(_("Home the machine after job is finished"))
        self.checkbox_autobeep.SetToolTip(_("Beep after the job is finished."))
        self.checkbox_autobeep.SetValue(1)
        self.checkbox_mock_usb.SetToolTip(
            _("DEBUG. Without a K40 connected continue to process things as if there was one."))
        self.checkbox_multiple_devices.SetToolTip(
            _("Specify matching criteria for the K40 to be used. Only matching K40 will be used."))
        self.spin_device_index.SetToolTip(_("-1 match anything. 0-5 match exactly that value."))
        self.spin_device_index.Enable(False)
        self.spin_device_address.SetToolTip(_("-1 match anything. 0-5 match exactly that value."))
        self.spin_device_address.Enable(False)
        self.spin_device_bus.SetToolTip(_("-1 match anything. 0-5 match exactly that value."))
        self.spin_device_bus.Enable(False)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Preferences.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_usb = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("USB Settings")), wx.VERTICAL)
        sizer_11 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_general = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("General Options")), wx.VERTICAL)
        sizer_bed = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("Bed Dimensions")), wx.HORIZONTAL)
        sizer_home = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("Shift Home Position")), wx.HORIZONTAL)
        sizer_speed = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("Speed Maximums")), wx.HORIZONTAL)
        sizer_board = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("Board Setup")), wx.HORIZONTAL)
        sizer_16 = wx.BoxSizer(wx.VERTICAL)
        sizer_17 = wx.BoxSizer(wx.VERTICAL)
        sizer_board.Add(self.combobox_board, 0, 0, 0)
        sizer_board.Add((20, 20), 0, 0, 0)
        sizer_17.Add(self.checkbox_1, 0, 0, 0)
        sizer_17.Add(self.checkbox_3, 0, 0, 0)
        sizer_board.Add(sizer_17, 1, wx.EXPAND, 0)
        sizer_16.Add(self.checkbox_2, 0, 0, 0)
        sizer_16.Add(self.checkbox_4, 0, 0, 0)
        sizer_board.Add(sizer_16, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_board, 1, wx.EXPAND, 0)
        label_13 = wx.StaticText(self, wx.ID_ANY, _("Vector"))
        sizer_speed.Add(label_13, 0, 0, 0)
        sizer_speed.Add(self.spin_speed_max, 0, 0, 0)
        label_15 = wx.StaticText(self, wx.ID_ANY, _("mm/s"))
        sizer_speed.Add(label_15, 0, 0, 0)
        sizer_speed.Add((20, 20), 0, 0, 0)
        label_14 = wx.StaticText(self, wx.ID_ANY, _("Raster"))
        sizer_speed.Add(label_14, 0, 0, 0)
        sizer_speed.Add(self.spin_speed_max_raster, 0, 0, 0)
        label_16 = wx.StaticText(self, wx.ID_ANY, _("mm/s"))
        sizer_speed.Add(label_16, 0, 0, 0)
        sizer_1.Add(sizer_speed, 1, wx.EXPAND, 0)
        label_9 = wx.StaticText(self, wx.ID_ANY, _("X"))
        sizer_home.Add(label_9, 0, 0, 0)
        sizer_home.Add(self.spin_home_x, 0, 0, 0)
        label_12 = wx.StaticText(self, wx.ID_ANY, _("mil"))
        sizer_home.Add(label_12, 0, 0, 0)
        sizer_home.Add((20, 20), 0, 0, 0)
        label_10 = wx.StaticText(self, wx.ID_ANY, _("Y"))
        sizer_home.Add(label_10, 0, 0, 0)
        sizer_home.Add(self.spin_home_y, 0, 0, 0)
        label_11 = wx.StaticText(self, wx.ID_ANY, _("mil"))
        sizer_home.Add(label_11, 0, 0, 0)
        sizer_home.Add((20, 20), 0, 0, 0)
        sizer_home.Add(self.button_home_by_current, 0, 0, 0)
        sizer_1.Add(sizer_home, 1, wx.EXPAND, 0)
        sizer_1.Add(self.radio_units, 1, wx.EXPAND, 0)
        label_2 = wx.StaticText(self, wx.ID_ANY, _("Width"))
        sizer_bed.Add(label_2, 0, 0, 0)
        sizer_bed.Add(self.spin_bedwidth, 0, 0, 0)
        label_17 = wx.StaticText(self, wx.ID_ANY, _("mm"))
        sizer_bed.Add(label_17, 0, 0, 0)
        sizer_bed.Add((20, 20), 0, 0, 0)
        label_3 = wx.StaticText(self, wx.ID_ANY, _("Height"))
        sizer_bed.Add(label_3, 0, 0, 0)
        sizer_bed.Add(self.spin_bedheight, 0, 0, 0)
        label_18 = wx.StaticText(self, wx.ID_ANY, _("mm"))
        sizer_bed.Add(label_18, 0, 0, 0)
        sizer_1.Add(sizer_bed, 0, wx.EXPAND, 0)
        sizer_general.Add(self.checkbox_autolock, 0, 0, 0)
        sizer_general.Add(self.checkbox_autohome, 0, 0, 0)
        sizer_general.Add(self.checkbox_autobeep, 0, 0, 0)
        sizer_1.Add(sizer_general, 1, wx.EXPAND, 0)
        sizer_usb.Add(self.checkbox_mock_usb, 0, 0, 0)
        sizer_usb.Add(self.checkbox_multiple_devices, 0, 0, 0)
        label_6 = wx.StaticText(self, wx.ID_ANY, _("Device Index:"))
        sizer_3.Add(label_6, 1, 0, 0)
        sizer_3.Add(self.spin_device_index, 1, 0, 0)
        sizer_usb.Add(sizer_3, 1, wx.EXPAND, 0)
        label_7 = wx.StaticText(self, wx.ID_ANY, _("Device Address:"))
        sizer_10.Add(label_7, 1, 0, 0)
        sizer_10.Add(self.spin_device_address, 1, 0, 0)
        sizer_usb.Add(sizer_10, 1, wx.EXPAND, 0)
        label_8 = wx.StaticText(self, wx.ID_ANY, _("Device Bus:"))
        sizer_11.Add(label_8, 1, 0, 0)
        sizer_11.Add(self.spin_device_bus, 1, 0, 0)
        sizer_usb.Add(sizer_11, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_usb, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def on_combobox_boardtype(self, event):  # wxGlade: Preferences.<event_handler>
        self.project.writer.board = self.combobox_board.GetValue()

    def on_check_flip_x(self, event):  # wxGlade: Preferences.<event_handler>
        print("Event handler 'on_check_flip_x' not implemented!")
        event.Skip()

    def on_check_home_right(self, event):  # wxGlade: Preferences.<event_handler>
        print("Event handler 'on_check_home_right' not implemented!")
        event.Skip()

    def on_check_flip_y(self, event):  # wxGlade: Preferences.<event_handler>
        print("Event handler 'on_check_flip_y' not implemented!")
        event.Skip()

    def on_check_home_bottom(self, event):  # wxGlade: Preferences.<event_handler>
        print("Event handler 'on_check_home_bottom' not implemented!")
        event.Skip()

    def spin_on_speed_vector_max(self, event):  # wxGlade: Preferences.<event_handler>
        print("Event handler 'spin_on_speed_vector_max' not implemented!")
        event.Skip()

    def spin_on_speed_raster_max(self, event):  # wxGlade: Preferences.<event_handler>
        print("Event handler 'spin_on_speed_raster_max' not implemented!")
        event.Skip()

    def spin_on_home_x(self, event):  # wxGlade: Preferences.<event_handler>
        print("Event handler 'spin_on_home_x' not implemented!")
        event.Skip()

    def spin_on_home_y(self, event):  # wxGlade: Preferences.<event_handler>
        print("Event handler 'spin_on_home_y' not implemented!")
        event.Skip()

    def on_button_set_home_current(self, event):  # wxGlade: Preferences.<event_handler>
        print("Event handler 'on_button_set_home_current' not implemented!")
        event.Skip()

    def on_radio_units(self, event):  # wxGlade: Preferences.<event_handler>
        if event.Int == 0:
            self.project.set_mm()
        elif event.Int == 1:
            self.project.set_cm()
        elif event.Int == 2:
            self.project.set_inch()
        elif event.Int == 3:
            self.project.set_mil()

    def spin_on_bedwidth(self, event):  # wxGlade: Preferences.<event_handler>
        self.project.size = self.spin_bedwidth.GetValue(), self.spin_bedheight.GetValue()
        self.project("bed_size", self.project.size)

    def spin_on_bedheight(self, event):  # wxGlade: Preferences.<event_handler>
        self.project.size = self.spin_bedwidth.GetValue(), self.spin_bedheight.GetValue()
        self.project("bed_size", self.project.size)

    def on_check_autolock(self, event):  # wxGlade: Preferences.<event_handler>
        self.project.writer.autolock = self.checkbox_autolock.GetValue()

    def on_check_autohome(self, event):  # wxGlade: Preferences.<event_handler>
        self.project.autohome = self.checkbox_autohome.GetValue()

    def on_check_autobeep(self, event):  # wxGlade: Preferences.<event_handler>
        self.project.autobeep = self.checkbox_autobeep.GetValue()

    def spin_on_device_index(self, event):  # wxGlade: Preferences.<event_handler>
        self.project.controller.usb_index = int(self.spin_device_index.GetValue())

    def spin_on_device_address(self, event):  # wxGlade: Preferences.<event_handler>
        self.project.controller.usb_address = int(self.spin_device_address.GetValue())

    def spin_on_device_bus(self, event):  # wxGlade: Preferences.<event_handler>
        self.project.controller.usb_bus = int(self.spin_device_bus.GetValue())

    def on_checkbox_mock_usb(self, event):  # wxGlade: Preferences.<event_handler>
        self.project.controller.mock = self.checkbox_mock_usb.GetValue()

    def on_checkbox_multiple_devices(self, event):  # wxGlade: Preferences.<event_handler>
        self.spin_device_index.Enable(self.checkbox_multiple_devices.GetValue())
        self.spin_device_bus.Enable(self.checkbox_multiple_devices.GetValue())
        self.spin_device_address.Enable(self.checkbox_multiple_devices.GetValue())
