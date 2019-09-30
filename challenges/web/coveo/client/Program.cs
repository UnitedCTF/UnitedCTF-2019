using Qml.Net;
using Qml.Net.Runtimes;

namespace united
{
    class Program
    {
        static int Main(string[] args)
        {
            RuntimeManager.DiscoverOrDownloadSuitableQtRuntime();
            
            QQuickStyle.SetStyle("Material");

            using (var application = new QGuiApplication(args))
            {
                using (var qmlEngine = new QQmlApplicationEngine())
                {
                    Qml.Net.Qml.RegisterType<QueryModel>("Features");

                    qmlEngine.Load("Main.qml");
                    
                    return application.Exec();
                }
            }
        }
    }
}
