// Runtime regression for the packaged catalog, including Qt's standard dialogs.
#include <QApplication>
#include <QAbstractButton>
#include <QDebug>
#include <QMessageBox>
#include <QTranslator>

int main(int argc, char **argv)
{
    QApplication app(argc, argv);
    QTranslator translator;
    if (argc != 2 || !translator.load(QString::fromLocal8Bit(argv[1])))
    {
        qCritical() << "Cannot load the built Chinese catalog";
        return 1;
    }
    app.installTranslator(&translator);
    QMessageBox box(QMessageBox::Question, "test", "test",
                    QMessageBox::Yes | QMessageBox::No | QMessageBox::Ok | QMessageBox::Cancel);
    for (auto button : { QMessageBox::Yes, QMessageBox::No, QMessageBox::Ok, QMessageBox::Cancel })
    {
        const QString text = box.button(button)->text();
        bool chinese = false;
        for (QChar c : text)
        {
            chinese |= c.unicode() >= 0x4e00 && c.unicode() <= 0x9fff;
        }
        if (!chinese)
        {
            qCritical() << "Untranslated standard button:" << text;
            return 2;
        }
    }
    for (auto context : { "Settings", "Event5", "Event8", "TableView" })
    {
        const char *source = QString(context) == "Settings" ? "Select Profile json"
                            : QString(context) == "TableView" ? "Save Output to CSV"
                                                              : "Select a wondercard file";
        if (QCoreApplication::translate(context, source) == QString::fromUtf8(source))
        {
            qCritical() << "Untranslated dialog:" << context << source;
            return 3;
        }
    }
    app.removeTranslator(&translator);
    if (QCoreApplication::translate("Settings", "Select Profile json") != "Select Profile json")
    {
        return 4;
    }
    qInfo() << "Chinese application and Qt standard-dialog translations passed; English fallback passed";
    return 0;
}
