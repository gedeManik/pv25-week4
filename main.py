from PyQt5 import QtWidgets, uic
import sys


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        uic.loadUi("design.ui", self)

        self.cart_total = 0

        self.pushButton.clicked.connect(self.add_to_cart)
        self.pushButton_2.clicked.connect(self.clear)

        self.show()

    def add_to_cart(self):
        product = self.comboBox.currentText()
        quantity = self.lineEdit.text()
        discount = self.comboBox_2.currentText()

        if quantity.isdigit():
            quantity = int(quantity)
            price = self.get_product_price(product)
            total_price = price * quantity

            if discount != "0%":
                discount_percentage = int(discount[:-1])
                discount_amount = total_price * (discount_percentage / 100)
                total_price -= discount_amount

            self.cart_total += total_price
            self.textBrowser.append(f"{product} - {quantity} x Rp. {price} ({discount})")
            self.label_4.setText(f"Total : Rp. {self.cart_total:,.0f}")
        else:
            self.textBrowser.append("Please enter a valid quantity.")

    def clear(self):
        self.comboBox.setCurrentIndex(0)
        self.lineEdit.clear()
        self.comboBox_2.setCurrentIndex(0)
        self.textBrowser.clear()
        self.cart_total = 0
        self.label_4.setText("Total : Rp. 0")

    def get_product_price(self, product):
        prices = {
            "Bimoli (Rp. 20,000)": 20000,
            "Beras 5 Kg (Rp. 75,000)": 75000,
            "Kecap ABC (Rp. 7,000)": 7000,
            "Saos Sachet (Rp. 2,500)": 2500
        }
        return prices.get(product, 0)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
