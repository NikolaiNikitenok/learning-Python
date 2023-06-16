import win32print
import win32api

# Создаем новый принтер
printer_name = "MyVirtualPrinter"
printer_driver_name = "Microsoft Print To PDF"
printer_port_name = "MyVirtualPrinterPort"
printer_device_name = "My Virtual Printer"
printer_info = {"Description": "My Virtual Printer", "Location": "Home"}
win32print.AddPrinterConnection(printer_name)

# Устанавливаем принтер по умолчанию
default_printer_name = win32print.GetDefaultPrinter()
if default_printer_name != printer_name:
    win32print.SetDefaultPrinter(printer_name)

# Создаем порт для принтера
win32print.AddPort(printer_port_name, win32print.PORT_TYPE_WRITE)

# Создаем устройство для принтера
device_mode = win32print.DEVMODE()
device_mode.Fields = ("dmFields", "dmDeviceName", "dmDriverName", "dmSpecVersion", "dmDriverVersion", "dmSize", "dmDriverExtra")
device_mode.dmFields = win32print.DM_SPECVERSION | win32print.DM_DRIVERVERSION | win32print.DM_SIZE
device_mode.dmDeviceName = printer_device_name
device_mode.dmDriverName = printer_driver_name
device_mode.dmSpecVersion = 1024
device_mode.dmDriverVersion = 1536
device_mode.dmSize = win32api.sizeof(device_mode)
win32print.AddPrinterDriver(printer_driver_name, device_mode)

# Связываем принтер с портом и устройством
win32print.SetPrinter(printer_name, None, {"PortName": printer_port_name, "DriverName": printer_driver_name, "Attributes": win32print.PRINTER_ATTRIBUTE_VIRTUAL, "DeviceMode": device_mode})

# Печатаем документ
file_path = "12ТМ.pdf"
job_title = "My Document"
job_options = {"Collate": True, "Duplex": win32print.DUPLEX_VERTICAL}
win32print.StartDocPrinter(printer_name, 1, (job_title,))
win32print.StartPagePrinter(printer_name)
win32print.WritePrinter(win32print.OpenPrinter(printer_name), open(file_path, "rb").read())
win32print.EndPagePrinter(printer_name)
win32print.EndDocPrinter(printer_name)
