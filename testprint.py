from escpos.printer import Usb
import time

try:
    print("Connecting to printer 1fc9:2014...")
    printer = Usb(0x1fc9, 0x2014)
    
    print("Sending test receipt...")
    
    # Simple test print
    printer.text("================\n")
    printer.text("  TEST RECEIPT  \n")
    printer.text("================\n\n")
    
    printer.text("Printer: NXP USB\n")
    printer.text("Device: 1fc9:2014\n")
    printer.text("Date: 2025-11-20\n")
    printer.text("Time: " + time.strftime("%H:%M:%S") + "\n\n")
    
    printer.text("Connection: OK\n")
    printer.text("Status: ONLINE\n\n")
    
    printer.text("================\n")
    printer.text(" Test Complete\n")
    printer.text("================\n\n")
    
    # Cut paper
    printer.cut()
    
    print("✓ Test receipt sent successfully!")
    print("✓ Check your printer for output")
    
except Exception as e:
    print("✗ Print failed!")
    print("Error:", str(e))
    import traceback
    traceback.print_exc()
