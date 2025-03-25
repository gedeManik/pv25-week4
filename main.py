import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QComboBox, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit)

class POSApplication(QWidget):
    def __init__(self):
        super().__init__()
        
        self.cart_total = 0
        self.initUI()

    def initUI(self): 
        self.resize(400, 300)
        self.productLabel = QLabel('Product:')
        self.quantityLabel = QLabel('Quantity:')
        self.discountLabel = QLabel('Discount:')

        self.productComboBox = QComboBox()
        self.productComboBox.addItems([
            "Bimoli (Rp. 20,000)",
            "Beras 5 Kg (Rp. 75,000)",
            "Kecap ABC (Rp. 7,000)",
            "Saos Saset (Rp. 2,500)"
        ])
        
        self.quantityInput = QLineEdit()
        self.quantityInput.setPlaceholderText('Enter quantity')

        self.discountComboBox = QComboBox()
        self.discountComboBox.addItems([
            "No Discount",
            "5%",
            "10%",
            "15%"
        ])

        self.addButton = QPushButton('Add to Cart')
        self.clearButton = QPushButton('Clear')

        self.outputText = QTextEdit()
        self.outputText.setReadOnly(True)

        self.totalLabel = QLabel('Total: Rp. 0')

        layout = QVBoxLayout()

        layout.addWidget(self.productLabel)
        layout.addWidget(self.productComboBox)

        layout.addWidget(self.quantityLabel)
        layout.addWidget(self.quantityInput)

        layout.addWidget(self.discountLabel)
        layout.addWidget(self.discountComboBox)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.addButton)
        buttonLayout.addWidget(self.clearButton)
        layout.addLayout(buttonLayout)

        layout.addWidget(self.outputText)
        layout.addWidget(self.totalLabel)

        self.setLayout(layout)

        self.addButton.clicked.connect(self.add_to_cart)
        self.clearButton.clicked.connect(self.clear)

        self.setWindowTitle('POS Application by F1D022046')
        self.show()

    def add_to_cart(self):
        product = self.productComboBox.currentText()
        quantity = self.quantityInput.text()
        discount = self.discountComboBox.currentText()

        if quantity.isdigit():
            quantity = int(quantity)
            price = self.get_product_price(product)
            total_price = price * quantity
            
            if discount != "No Discount":
                discount_percentage = int(discount[:-1])
                discount_amount = total_price * (discount_percentage / 100)
                total_price -= discount_amount

            self.cart_total += total_price

            self.outputText.append(f"{product} - {quantity} x Rp. {price} ({discount})")
            self.totalLabel.setText(f'Total: Rp. {self.cart_total:,.0f}')
        else:
            self.outputText.append("Please enter a valid quantity.")

    def clear(self):
        self.productComboBox.setCurrentIndex(0)
        self.quantityInput.clear()
        self.discountComboBox.setCurrentIndex(0)
        self.outputText.clear()
        self.cart_total = 0  
        self.totalLabel.setText('Total: Rp. 0')

    def get_product_price(self, product):
        prices = {
            "Bimoli (Rp. 20,000)": 20000,
            "Beras 5 Kg (Rp. 75,000)": 75000,
            "Kecap ABC (Rp. 7,000)": 7000,
            "Saos Saset (Rp. 2,500)": 2500
        }
        return prices.get(product, 0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = POSApplication()
    sys.exit(app.exec_())
