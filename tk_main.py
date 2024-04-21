import tkinter as tk
import req_vendor

app = tk.Tk()
label = tk.Label(app, text="Click the button")


def show_vendor_info():
    uri = get_uri()
    vendor = req_vendor.get_vendor(uri)
    vendor_address = vendor["vendor_address"]
    vendor_fax = vendor["vendor_fax"]
    vendor_name = vendor["vendor_name"]
    label.config(text=vendor_address)


def get_uri():
    return str('/1')


def tk_open():
    app.title("Tkinter with Machine!")
    app.geometry("800x450")
    label.pack(pady=10)
    button = tk.Button(app, text='start', command=show_vendor_info)
    button.pack()

    app.mainloop()


if __name__ == '__main__':
    tk_open()
