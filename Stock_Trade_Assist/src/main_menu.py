from PyQt5 import QtCore, QtGui, QtWidgets
from selector_menu import Ui_selectorWindow
from buy_call import Ui_callGenerationWindow
from screener_result import Ui_screenerResultWindow
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd
import datetime as dt
import yfinance as yf
import talib
import json
import itertools

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Designing phase
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(570, 410)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setStyleSheet("QWidget {\n"
        "    background-color: #17181c;\n"
        "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Button for Screener
        self.screenerButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.open_screener())
        self.screenerButton.setGeometry(QtCore.QRect(180, 70, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.screenerButton.setFont(font)
        self.screenerButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.screenerButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.screenerButton.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(255, 255, 255) ; \n"
        "    border-radius: 15px;\n"
        "    border: 3px solid #4CAF50;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "  background-color: #4CAF50; \n"
        "  color: white;\n"
        "  border: 3px solid rgb(255, 255, 255);\n"
        "}\n"
        "")
        self.screenerButton.setIconSize(QtCore.QSize(16, 16))
        self.screenerButton.setObjectName("screenerButton")

        # Button for Trader
        self.tradeButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.open_trader())
        self.tradeButton.setGeometry(QtCore.QRect(180, 140, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.tradeButton.setFont(font)
        self.tradeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tradeButton.setMouseTracking(False)
        self.tradeButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tradeButton.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(255, 255, 255) ; \n"
        "    border-radius: 15px;\n"
        "    border: 3px solid #4CAF50;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "  background-color: #4CAF50; \n"
        "  color: white;\n"
        "  border: 3px solid rgb(255, 255, 255);\n"
        "}\n"
        "")
        self.tradeButton.setObjectName("tradeButton")

        # Button for Swing Trade
        self.swingTradeButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.open_swing_trader())
        self.swingTradeButton.setGeometry(QtCore.QRect(180, 200, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.swingTradeButton.setFont(font)
        self.swingTradeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.swingTradeButton.setMouseTracking(False)
        self.swingTradeButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.swingTradeButton.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(255, 255, 255) ; \n"
        "    border-radius: 15px;\n"
        "    border: 3px solid #4CAF50;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "  background-color: #4CAF50; \n"
        "  color: white;\n"
        "  border: 3px solid rgb(255, 255, 255);\n"
        "}\n"
        "")
        self.swingTradeButton.setObjectName("swingTradeButton")

        # Button for Aniticipatory Trade
        self.anticipatoryTradeButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.open_aniticipatory_trader())
        self.anticipatoryTradeButton.setGeometry(QtCore.QRect(180, 270, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.anticipatoryTradeButton.setFont(font)
        self.anticipatoryTradeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.anticipatoryTradeButton.setMouseTracking(False)
        self.anticipatoryTradeButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.anticipatoryTradeButton.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(255, 255, 255) ; \n"
        "    border-radius: 15px;\n"
        "    border: 3px solid #4CAF50;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "  background-color: #4CAF50; \n"
        "  color: white;\n"
        "  border: 3px solid rgb(255, 255, 255);\n"
        "}\n"
        "")
        self.anticipatoryTradeButton.setObjectName("anticipatoryTradeButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 570, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

# working phase
    def open_selector_menu(self,type):
        self.screener_window = QtWidgets.QMainWindow()
        self.ui = Ui_selectorWindow()
        self.ui.setupUi(self.screener_window, MainWindow)
        self.set_mainComboBox(type)
        self.screener_window.show()
        MainWindow.hide()
        self.done = True

    def open_buy_call_menu(self):
        self.buy_call_window = QtWidgets.QMainWindow()
        self.ui_buy_call = Ui_callGenerationWindow()
        self.ui_buy_call.setupUi(self.buy_call_window, MainWindow, self.screener_window)

    def open_screener_result_menu(self):
        self.screener_result_window = QtWidgets.QMainWindow()
        self.ui_screener_result = Ui_screenerResultWindow()
        self.ui_screener_result.setupUi(self.screener_result_window, self.screener_window)

    def set_mainComboBox(self,type):
        self.ui.submitButton.setEnabled(False)
        self.ui.enableCompanySelectionCheckBox.setVisible(False)
        main_list = ["Broad Index", "Sectoral Index", "Capital Index"]
        self.ui.mainComboBox.addItems(main_list)
        self.ui.subComboBox.setVisible(False)
        self.ui.companyComboBox.setVisible(False)
        self.ui.mainComboBox.activated.connect(lambda: self.set_subComboBox(type))

    def set_subComboBox(self,type):
        self.ui.subComboBox.setVisible(True)
        self.ui.submitButton.setEnabled(True)
        if type == "screener":
            self.ui.enableCompanySelectionCheckBox.setVisible(False)
            self.ui.subComboBox.clear()
        else:
            self.ui.enableCompanySelectionCheckBox.setVisible(True)
            self.ui.subComboBox.clear()
            self.ui.companyComboBox.clear()
        mainComboBox_entered_value = self.ui.mainComboBox.currentText()
        self.broad_list = ['NIFTY50', 'NIFTY NEXT 50', 'NIFTY100', 'NIFTY200', 'NIFTY500']
        self.sectoral_list = ['NIFTY BANK', 'NIFTY FINANCE', 'NIFTY FMCG', 'NIFTY IT', 'NIFTY HEALTHCARE', 'NIFTY ONG', 'NIFTY METAL', 'NIFTY PHARMA']
        self.capital_list = ['NIFTY MIDCAP 150', 'NIFTY SMALLCAP 250', 'NIFTY MICROCAP 250']

        if mainComboBox_entered_value == "Broad Index":
            self.ui.subComboBox.addItems(self.broad_list)
        if mainComboBox_entered_value == "Sectoral Index":
            self.ui.subComboBox.addItems(self.sectoral_list)
        if mainComboBox_entered_value == "Capital Index":
            self.ui.subComboBox.addItems(self.capital_list)
        self.ui.subComboBox.activated.connect(self.set_companyComboBox)

    def set_value_for_companyComboBox(self,i):
        subComboBox_entered_value = self.ui.subComboBox.currentText()
        is_found = False
        if subComboBox_entered_value == i:
            is_found = True
            text_file = i + '.txt'
            with open(text_file) as f:
                data = f.read()
            tickers = json.loads(data)
            company_list = []
            for i in tickers:
                ticker = tickers[i]
                company_list.append(list(tickers.keys())[list(tickers.values()).index(ticker)])
            self.ui.companyComboBox.addItems(company_list)
        return is_found

    def set_companyComboBox(self):
        if self.ui.enableCompanySelectionCheckBox.isChecked() == True:
            self.ui.companyComboBox.clear()
            self.ui.companyComboBox.setVisible(True)
            for i in self.broad_list:
                if not self.set_value_for_companyComboBox(i):
                    for i in self.sectoral_list:
                        if not self.set_value_for_companyComboBox(i):
                            for i in self.capital_list:
                                self.set_value_for_companyComboBox(i)
        else:
            self.ui.companyComboBox.setEnabled(False)

    def open_screener(self):
        self.open_selector_menu("screener")
        if self.done == True:
            self.ui.enableCompanySelectionCheckBox.hide()
            self.ui.companyComboBox.hide()
            self.ui.submitButton.clicked.connect(self.screener)

    def open_trader(self):
        self.type = "trade"
        self.open_selector_menu(" ")
        if self.done == True:
            self.ui.submitButton.clicked.connect(lambda: self.trade(self.type))

    def open_swing_trader(self):
        self.type = "swing"
        self.open_selector_menu(" ")
        if self.done == True:
            self.ui.submitButton.clicked.connect(lambda: self.trade(self.type))

    def open_aniticipatory_trader(self):
        self.open_selector_menu(" ")
        if self.done == True:
            self.ui.submitButton.clicked.connect(self.anticipatory_trade)

    def screener(self):
        self.open_screener_result_menu()
        self.start = dt.datetime.now() - dt.timedelta(days=365)
        self.end = dt.datetime.now()
        self.index = self.ui.subComboBox.currentText()
        text_file = self.index + '.txt'
        with open(text_file) as f:
            data = f.read()
        self.tickers = json.loads(data)

        nifty50 = yf.download('^NSEI', self.start, self.end)
        nifty50['Percentage Change'] = nifty50['Close'].pct_change()
        nifty50_returns = (nifty50['Percentage Change'] + 1).cumprod()[-1]

        ticker_list = []
        return_list = []
        try:
            for i in self.tickers:
                ticker = self.tickers[i]
                df = yf.download(ticker, self.start, self.end)
                df['Pct Change'] = df['Close'].pct_change()
                stock_return = (df['Pct Change'] + 1).cumprod()[-1]
                return_compared = round((stock_return / nifty50_returns), 2)
                ticker_list.append(ticker)
                return_list.append(return_compared)
        except Exception:
            print("No data on ")

        self.best = pd.DataFrame(list(zip(ticker_list, return_list)), columns=['Ticker', 'Returns'])
        self.best['RS'] = self.best['Returns'].rank(pct=True) * 100
        # Condition 8
        self.best = self.best[self.best['RS'] > 70]
        self.screener_strategy()

    def screener_strategy(self):
        final_list = []
        for i in self.best.index:
            ticker = self.best['Ticker'][i]
            try:
                df = yf.download(ticker, self.start, self.end)
                smaUsed = [50, 150, 200]
                for x in smaUsed:
                    sma = x
                    df["SMA_" + str(sma)] = round(df['Close'].rolling(window=sma).mean(), 2)

                df["EMA_200"] = round(df.Close.ewm(span=200, adjust=False).mean(), 2)

                currentClose = df["Close"][-1]
                moving_average_50 = df["SMA_50"][-1]
                moving_average_150 = df["SMA_150"][-1]
                moving_average_200 = df["SMA_200"][-1]
                low_of_52week = min(df["Close"][-260:])
                high_of_52week = max(df["Close"][-260:])

                try:
                    moving_average_200_20 = df["SMA_200"][-20]

                except Exception:
                    moving_average_200_20 = 0

                # Condition 1: Current Price > 150 SMA and > 200 SMA
                if (currentClose > moving_average_150 > moving_average_200):
                    cond_1 = True
                else:
                    cond_1 = False
                # Condition 2: 150 SMA and > 200 SMA
                if (moving_average_150 > moving_average_200):
                    cond_2 = True
                else:
                    cond_2 = False
                # Condition 3: 200 SMA trending up for at least 1 month (ideally 4-5 months)
                if (moving_average_200 > moving_average_200_20):
                    cond_3 = True
                else:
                    cond_3 = False
                # Condition 4: 50 SMA> 150 SMA and 50 SMA> 200 SMA
                if (moving_average_50 > moving_average_150 > moving_average_200):
                    # print("Condition 4 met")
                    cond_4 = True
                else:
                    # print("Condition 4 not met")
                    cond_4 = False
                # Condition 5: Current Price > 50 SMA
                if (currentClose > moving_average_50):
                    cond_5 = True
                else:
                    cond_5 = False
                # Condition 6: Current Price is at least 30% above 52 week low (Many of the best are up 100-300% before coming out of consolidation)
                if (currentClose >= (1.3 * low_of_52week)):
                    cond_6 = True
                else:
                    cond_6 = False
                # Condition 7: Current Price is within 25% of 52 week high
                if (currentClose >= (.75 * high_of_52week)):
                    cond_7 = True
                else:
                    cond_7 = False
                # Condition 8: RS rating >70 and the higher the better already checked at the beginning
                if (cond_1 and cond_2 and cond_3 and cond_4 and cond_5 and cond_6 and cond_7):
                    final_list.append(self.best['Ticker'][i])
            except Exception:
                pass
        print(final_list)
        self.ff_list = []
        for i in final_list:
            ticker = str(i)
            try:
                quarter = info.get_earnings(ticker)
                quarterly_result = list(quarter['quarterly_revenue_earnings']['earnings'])
                if quarterly_result[-1] > quarterly_result[-2]:
                    self.ff_list.append(ticker)
            except Exception:
                self.ff_list.append(ticker)
        print(self.ff_list)
        self.companies = []
        for i in self.ff_list:
            self.companies.append(list(self.tickers.keys())[list(self.tickers.values()).index(i)])
        print(self.companies)
        self.screener_result_window.show()
        self.screener_window.hide()
        if len(self.ff_list) == 0:
            self.ui_screener_result.resultComboBox.addItem("None")
            self.ui_screener_result.canBuyButton.setDisabled(True)
        else:
            self.ui_screener_result.resultComboBox.addItems(self.companies)
            self.ui_screener_result.canBuyButton.clicked.connect(lambda: self.trade("screen"))

    def trade(self,trade_type):
        self.start = dt.datetime.now() - dt.timedelta(days=365)
        self.end = dt.datetime.now()
        self.index = self.ui.subComboBox.currentText()
        text_file = self.index + '.txt'
        with open(text_file) as f:
            data = f.read()
        tickers = json.loads(data)
        if self.ui.enableCompanySelectionCheckBox.isChecked() == True:
            self.open_buy_call_menu()
            self.company_name = self.ui.companyComboBox.currentText()
            self.company_ticker = tickers[self.company_name]
            self.ui_buy_call.nextPushButton.hide()
            self.ui_buy_call.prevPushButton.hide()
            if trade_type == "swing":
                try:
                    self.swing_trade_strategy()
                except Exception:
                    print("err")
            elif trade_type == "trade":
                try:
                    self.trade_strategy()
                except Exception:
                    print("err")

            if self.buy == True:
                self.ui_buy_call.callLabel.setText(f"Buy - {self.company_name}")
                self.ui_buy_call.displayTargetLabel.setText(self.target)
            else:
                self.ui_buy_call.callLabel.setText("No Buy call generated")
                self.ui_buy_call.displayTargetLabel.setText("-")
                self.ui_buy_call.displayStopLossLabel.setText("-")
        else:
            self.trade_list = []
            self.target_price_list = []
            self.stoploss_list = []
            self.open_buy_call_menu()
            if trade_type == "screen":
                if self.ui_screener_result.selectAllCheckBox.isChecked() == True:
                    for i in self.companies:
                        self.company_ticker = self.tickers[i]
                        try:
                            self.trade_strategy()
                        except Exception:
                            print("err")

                        if self.buy == True:
                            self.trade_list.append(i)
                            self.target_price_list.append(self.target)
                            self.stoploss_list.append(self.stoploss)
                else:
                    self.ui_buy_call.nextPushButton.hide()
                    self.ui_buy_call.prevPushButton.hide()
                    self.company_name = self.ui_screener_result.resultComboBox.currentText()
                    self.company_ticker = self.tickers[self.company_name]
                    try:
                        self.trade_strategy()
                    except Exception:
                        print("err")
                    if self.buy == True:
                        self.ui_buy_call.callLabel.setText(f"Buy - {self.company_name}")
                        self.ui_buy_call.displayTargetLabel.setText(self.target)
                    else:
                        self.ui_buy_call.callLabel.setText("No Buy call generated")
                        self.ui_buy_call.displayTargetLabel.setText("-")
                        self.ui_buy_call.displayStopLossLabel.setText("-")
            else:
                self.index = self.ui.subComboBox.currentText()
                company_counter = 0
                for i in tickers:
                    self.company_ticker = tickers[i]
                    company_counter += 1
                    if trade_type == "swing":
                        try:
                            self.swing_trade_strategy()
                        except Exception:
                            if company_counter == 1:
                                print("check ur connection")
                                break
                            else:
                                pass

                    elif trade_type == "trade":
                        try:
                            self.trade_strategy()
                        except Exception:
                            if company_counter == 1:
                                print("check ur connection")
                                break
                            else:
                                pass

                    if self.buy == True:
                        self.trade_list.append(i)
                        self.target_price_list.append(self.target)
                        self.stoploss_list.append(self.stoploss)

            if len(self.trade_list) == 0:
                self.ui_buy_call.nextPushButton.hide()
                self.ui_buy_call.prevPushButton.hide()
                self.ui_buy_call.callLabel.setText("No Buy call generated")
                self.ui_buy_call.displayTargetLabel.setText("-")
                self.ui_buy_call.displayStopLossLabel.setText("-")
            else:
                self.buy_count = 0
                self.ui_buy_call.callLabel.setText(f"Buy - {self.trade_list[self.buy_count]}")
                self.ui_buy_call.displayTargetLabel.setText(str(self.target))
                self.ui_buy_call.displayStopLossLabel.setText(str(self.stoploss))
                self.ui_buy_call.nextPushButton.clicked.connect(lambda: self.show_next(self.trade_list, self.target_price_list, self.stoploss_list))
                self.ui_buy_call.prevPushButton.clicked.connect(lambda: self.show_prev(self.trade_list, self.target_price_list, self.stoploss_list))
        self.buy_call_window.show()
        self.screener_window.hide()

    def show_next(self, company_list, target_list, stoploss_list):
        self.len = len(company_list)
        self.buy_count += 1
        if self.buy_count < self.len:
            self.ui_buy_call.callLabel.setText(f"Buy - {company_list[self.buy_count]}")
            self.ui_buy_call.displayTargetLabel.setText(str(target_list[self.buy_count]))
            self.ui_buy_call.displayStopLossLabel.setText(str(stoploss_list[self.buy_count]))
        else:
            self.buy_count = 0
            self.ui_buy_call.callLabel.setText(f"Buy - {company_list[self.buy_count]}")
            self.ui_buy_call.displayTargetLabel.setText(str(target_list[self.buy_count]))
            self.ui_buy_call.displayStopLossLabel.setText(str(stoploss_list[self.buy_count]))

    def show_prev(self, company_list, target_list, stoploss_list):
        self.len = len(company_list)
        self.buy_count -= 1
        if self.buy_count >= 0:
            self.ui_buy_call.callLabel.setText(f"Buy - {company_list[self.buy_count]}")
            self.ui_buy_call.displayTargetLabel.setText(str(target_list[self.buy_count]))
            self.ui_buy_call.displayStopLossLabel.setText(str(stoploss_list[self.buy_count]))
        else:
            self.buy_count = self.len-1
            self.ui_buy_call.callLabel.setText(f"Buy - {company_list[self.buy_count]}")
            self.ui_buy_call.displayTargetLabel.setText(str(target_list[self.buy_count]))
            self.ui_buy_call.displayStopLossLabel.setText(str(stoploss_list[self.buy_count]))

    def swing_trade_strategy(self):
        self.df = yf.download(self.company_ticker, start=self.start, end=self.end)
        self.MACD()
        self.RSI()
        self.buy = False
        self.target = "-"
        self.stoploss = "-"
        if self.df['MACD'][-1] > self.df['MACD_Signal'][-1]:
           if self.df['MACD_hist'][-2] <= 0:
                # Check RSI
                if self.df['RSI'][-1] >= self.df['EMA_14'][-1] or self.df['RSI'][-1] > 60:
                    self.buy = True
                    self.stoploss = "Trailing Stop Loss"

    def trade_strategy(self):
        self.df = yf.download(self.company_ticker, start=self.start, end=self.end)
        self.MACD()
        self.RSI()
        self.BB()
        self.fibonacci()
        self.key_moving_average()
        self.buy = False
        self.target = "-"
        self.stoploss = "-"

        current_price = self.df['Close'][-1]
        # Trend detection
        trendline = self.df.Close.ewm(span=200, adjust=False).mean()
        # Strategy
        if current_price < trendline[-1]:
            print("below")
            higher_limit = self.lower_band[-1] + self.lower_band[-1] * .05
            lower_limit = self.lower_band[-1] - self.lower_band[-1] * .05

            if (higher_limit > current_price) and (lower_limit < current_price):
                df_for_pattern = self.df.tail(5)
                engulf = talib.CDLENGULFING(df_for_pattern['Open'], df_for_pattern['High'], df_for_pattern['Low'], df_for_pattern['Close'])
                morning_star = talib.CDLMORNINGDOJISTAR(df_for_pattern['Open'], df_for_pattern['High'], df_for_pattern['Low'], df_for_pattern['Close'])
                hammer = talib.CDLHAMMER(df_for_pattern['Open'], df_for_pattern['High'], df_for_pattern['Low'], df_for_pattern['Close'])

                count = -1
                bullish_found = False
                for (i, j, k) in (zip(reversed(engulf), reversed(morning_star), reversed(hammer))):
                    if i == 100 or j == 100 or k == 100:
                        # index position of pattern formed date
                        position = count
                        bullish_found = True
                        break
                    else:
                        count -= 1
                # volume on pattern formed day
                if bullish_found == True:
                    volume_on_pattern = self.df['Volume'][position]
                    # Check Volume
                    if volume_on_pattern >= (self.df['Volume'][position - 1] - (self.df['Volume'][position - 1] * 0.05)):
                        # Check RSI
                        if self.df['RSI'][-1] >= 60 or self.df['RSI'][-1] > self.df['EMA_14'][-1]:
                            # Check MACD crossover
                            if self.df['MACD'][-1] > self.df['MACD_Signal'][-1]:
                                self.buy = True
                                self.target = round(upper_band)
                                self.stoploss = round(lower_limit)

        else:
            print("above")
            # fibinacci level adjust
            first_level_lower_bound = self.first_level - (self.first_level * 0.05)
            first_level_upper_bound = self.first_level + (self.first_level * 0.05)
            max_price_lower_bound = self.max_price - (self.max_price * 0.05)
            max_price_upper_bound = self.max_price + (self.max_price * 0.05)

            if first_level_lower_bound < current_price and current_price < first_level_upper_bound:
                print("first level")
                # Check MACD Crossover
                if self.df['MACD'][-1] > self.df['MACD_Signal'][-1]:
                    print("macd")
                    if self.df['MACD_hist'][-1] > self.df['MACD_hist'][-2]:
                        # Check Moving Average Crossover
                        if self.df['signal_EMA'][-1] > self.df['anticipation_EMA'][-1]:
                            print("sma")
                            # Check RSI
                            if self.df['RSI'][-1] >= 60:
                                print("RSI")
                                self.buy = True
                                self.target = "MACD bearish crossover"
                                self.stoploss = round(first_level_lower_bound)

            elif max_price_lower_bound < current_price and current_price < max_price_upper_bound:
                print("max level")
                df_for_pattern = self.df.tail(5)
                engulf = talib.CDLENGULFING(df_for_pattern['Open'], df_for_pattern['High'], df_for_pattern['Low'], df_for_pattern['Close'])
                morning_star = talib.CDLMORNINGDOJISTAR(df_for_pattern['Open'], df_for_pattern['High'], df_for_pattern['Low'], df_for_pattern['Close'])
                shooting_star = talib.CDLSHOOTINGSTAR(df_for_pattern['Open'], df_for_pattern['High'], df_for_pattern['Low'], df_for_pattern['Close'])
                hanging_man = talib.CDLHANGINGMAN(df_for_pattern['Open'], df_for_pattern['High'], df_for_pattern['Low'], df_for_pattern['Close'])
                hammer = talib.CDLHAMMER(df_for_pattern['Open'], df_for_pattern['High'], df_for_pattern['Low'], df_for_pattern['Close'])

                bearish_found = False
                for (i, j, k) in (zip(reversed(engulf), reversed(shooting_star), reversed(hanging_man))):
                    if i == -100 or j == 100 or k == 100:
                        print("bearish found")
                        bearish_found = True
                        break

                if bearish_found == False:
                    count = -1
                    bullish_found = False
                    for (i, j, k) in (zip(reversed(engulf), reversed(morning_star), reversed(hammer))):
                        if i == 100 or j == 100 or k == 100:
                            # index position of pattern formed date
                            print("bullish found")
                            position = count
                            bullish_found = True
                            break
                        else:
                            count -= 1

                    if bullish_found == True:
                        volume_on_pattern = self.df['Volume'][position]
                        # Check Volume
                        avg_volume = (self.df['Volume'][position - 1] + self.df['Volume'][position - 2] + self.df['Volume'][position - 3] + self.df['Volume'][position - 4] + self.df['Volume'][position - 5]) / 5
                        if volume_on_pattern >= (avg_volume - avg_volume * 0.05):
                            print("volume")
                            # Check RSI
                            if self.df['RSI'][-1] >= 60:
                                print("rsi")
                                # Check MACD crossover
                                if self.df['MACD'][-1] > self.df['MACD_Signal'][-1]:
                                    print("macd")
                                    self.buy = True
                                    target_cal = max_price + (max_price - first_level)
                                    self.target = round(target_cal - target_cal * 0.05)
                                    self.stoploss = round(max_price_lower_bound)

    def anticipatory_trade(self):
        self.open_buy_call_menu()
        self.ui_buy_call.targetLabel.setText("Anticipatory Call")
        self.ui_buy_call.stopLossLabel.hide()
        self.ui_buy_call.displayStopLossLabel.hide()
        self.start = dt.datetime.now() - dt.timedelta(days=365)
        self.end = dt.datetime.now()
        self.end_needed = dt.datetime.now() + dt.timedelta(days=5)
        self.delta = dt.timedelta(days=1)
        self.index = self.ui.subComboBox.currentText()
        text_file = self.index + '.txt'
        with open(text_file) as f:
            data = f.read()
        tickers = json.loads(data)
        if self.ui.enableCompanySelectionCheckBox.isChecked() == True:
            self.company_name = self.ui.companyComboBox.currentText()
            self.company_ticker = tickers[self.company_name]
            self.ui_buy_call.nextPushButton.hide()
            self.ui_buy_call.prevPushButton.hide()
            try:
                self.anticipatory_trade_strategy()
            except Exception:
                print("err")

            if self.buy == True:
                self.ui_buy_call.callLabel.setText(f"Buy - {self.company_name}")
                self.ui_buy_call.displayTargetLabel.setText(f"{self.count} days")
            else:
                self.ui_buy_call.callLabel.setText("No Buy call generated")
                self.ui_buy_call.displayTargetLabel.setText("-")

        else:
            self.index = self.ui.subComboBox.currentText()
            self.trade_list = []
            self.day_count_list = []
            company_counter = 0
            for i in tickers:
                self.company_ticker = tickers[i]
                company_counter += 1
                try:
                    self.anticipatory_trade_strategy()
                except Exception:
                    if company_counter == 1:
                        print("check ur connection")
                        break
                    else:
                        pass

                if self.buy == False:
                    self.trade_list.append(i)
                    self.day_count_list.append(self.result_count)

            if len(self.trade_list) == 0:
                self.ui_buy_call.callLabel.setText("No Buy call generated")
                self.ui_buy_call.displayTargetLabel.setText("-")
            else:
                self.buy_count = 0
                self.ui_buy_call.callLabel.setText(f"Buy - {self.trade_list[self.buy_count]}")
                self.ui_buy_call.displayTargetLabel.setText(f"{self.day_count_list[self.buy_count]} days")
                self.ui_buy_call.nextPushButton.clicked.connect(lambda: self.show_next_anticipation(self.trade_list, self.day_count_list))
                self.ui_buy_call.prevPushButton.clicked.connect(lambda: self.show_prev_anticipation(self.trade_list, self.day_count_list))
        self.buy_call_window.show()
        self.screener_window.hide()

    def show_next_anticipation(self, company_list, day_list):
        self.len = len(company_list)
        self.buy_count += 1
        if self.buy_count < self.len:
            self.ui_buy_call.callLabel.setText(f"Buy - {company_list[self.buy_count]}")
            self.ui_buy_call.displayTargetLabel.setText(f"{day_list[self.buy_count]} days")
        else:
            self.buy_count = 0
            self.ui_buy_call.callLabel.setText(f"Buy - {company_list[self.buy_count]}")
            self.ui_buy_call.displayTargetLabel.setText(f"{day_list[self.buy_count]} days")

    def show_prev_anticipation(self, company_list, day_list):
        self.len = len(company_list)
        self.buy_count -= 1
        if self.buy_count >= 0:
            self.ui_buy_call.callLabel.setText(f"Buy - {company_list[self.buy_count]}")
            self.ui_buy_call.displayTargetLabel.setText(f"{day_list[self.buy_count]} days")
        else:
            self.buy_count = self.len-1
            self.ui_buy_call.callLabel.setText(f"Buy - {company_list[self.buy_count]}")
            self.ui_buy_call.displayTargetLabel.setText(f"{day_list[self.buy_count]} days")

    def anticipatory_trade_strategy(self):
        self.df = yf.download(self.company_ticker, start=self.start, end=self.end)
        new_df = self.df.filter(['Close'])
        pred_model = load_model('Predictor.h5')
        while (self.end < self.end_needed):
            scaler = MinMaxScaler(feature_range=(0, 1))
            last_60_days = new_df[-60:].values
            last_60_days_scaled = scaler.fit_transform(last_60_days)
            X_test = []
            X_test.append(last_60_days_scaled)
            X_test = np.array(X_test)
            X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

            pred_price = pred_model.predict(X_test)
            pred_price = scaler.inverse_transform(pred_price)
            pred_price = pred_price.flatten()
            pred_price = pred_price[0]
            self.end += self.delta
            append_df = [{'Close': pred_price}]
            new_df = new_df.append(append_df)
            self.df = new_df

        self.MACD()
        self.buy = False
        self.count = 0
        self.result_count = 0
        day_list = [-5, -4, -3, -2, -1]
        for i in day_list:
            if new_df['MACD'].iloc[i] > new_df['MACD_Signal'].iloc[i - 1]:
                self.count += 1
                if new_df['MACD_hist'].iloc[i - 1] <= 0:
                    self.result_count = self.count
                    self.buy = True
                    break

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.screenerButton.setText(_translate("MainWindow", "SCREENER"))
        self.tradeButton.setText(_translate("MainWindow", "TRADE"))
        self.swingTradeButton.setText(_translate("MainWindow", "SWING TRADE"))
        self.anticipatoryTradeButton.setText(_translate("MainWindow", "ANTICIPATORY TRADE"))

    def MACD(self):
        self.shortEMA = self.df.Close.ewm(span=12, adjust=False).mean()
        self.longEMA = self.df.Close.ewm(span=26, adjust=False).mean()

        MACD = self.shortEMA - self.longEMA
        MACD_signal = MACD.ewm(span=9, adjust=False).mean()
        MACD_histogram = MACD - MACD_signal

        self.df['MACD'] = MACD
        self.df['MACD_Signal'] = MACD_signal
        self.df['MACD_hist'] = MACD_histogram

    def RSI(self):
        delta = self.df['Close'].diff(1)
        delta.dropna(inplace=True)

        positive = delta.copy()
        negative = delta.copy()

        positive[positive < 0] = 0
        negative[negative > 0] = 0

        EMA_14 = self.df.Close.ewm(span=14, adjust=False).mean()
        rsi_days = 14

        average_gain = positive.rolling(window=rsi_days).mean()
        average_loss = abs(negative.rolling(window=rsi_days).mean())

        relative_strength = average_gain / average_loss
        Relative_Strength_Index = 100.0 - (100 / (1.0 + relative_strength))

        self.df['EMA_14'] = EMA_14
        self.df['RSI'] = Relative_Strength_Index

    def BB(self):
        bollinger_period = 20
        std_dev_steps = 2
        bb_SMA = self.df.Close.rolling(window=bollinger_period).mean()
        std_dev = self.df.Close.rolling(window=bollinger_period).std()
        self.upper_band = bb_SMA + (std_dev_steps * std_dev)
        self.lower_band = bb_SMA - (std_dev_steps * std_dev)

    def fibonacci(self):
        self.max_price = self.df['Close'].max()
        self.min_price = self.df['Close'].min()

        diff = self.max_price - self.min_price
        self.first_level = self.max_price - (diff * 0.236)

    def key_moving_average(self):
        self.signal_EMA = self.df.Close.ewm(span=5, adjust=False).mean()
        self.anticipation_EMA = self.df.Close.ewm(span=13, adjust=False).mean()
        self.confirmation_EMA = self.df.Close.ewm(span=26, adjust=False).mean()
        self.df['signal_EMA'] = self.signal_EMA
        self.df['anticipation_EMA'] = self.anticipation_EMA
        self.df['confirmation_EMA'] = self.confirmation_EMA

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
