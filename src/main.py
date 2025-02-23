from gui.main_window import MainWindow
# from optionscli.options_alarm import SetOptions
import asyncio

async def main():
    main_window = MainWindow()
    await main_window.mainloop()

if __name__ == '__main__':
    asyncio.run(main())