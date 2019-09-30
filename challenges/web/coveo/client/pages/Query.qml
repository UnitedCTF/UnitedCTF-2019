import QtQuick 2.6
import QtQuick.Controls 2.1
import QtQuick.Window 2.2
import Features 1.0

ScrollablePage {
    Column {
        id:scrolled
        spacing: 5
        width: parent.width
        
        Label {
            width: parent.width
            wrapMode: Label.Wrap
            horizontalAlignment: Qt.AlignHCenter
            text: "This page perform a query to the super secure(obscure) server."
        }
        Button {
            width: parent.width
            text: 'Perform bitchain-enabled AI query'
            onClicked: {
                model.reset();
                var task = model.runQueryTask()
                Net.await(task, function(result) {
                    var data_to_show = result.split(',');
                    data_to_show.forEach(function(element) {
                       model.addSearchResult(element);
                    });
                    repeater.model = Net.toListModel(model.results);
                });
            }
        }
        Repeater {
            id: repeater
            Column {
                Rectangle {
                    anchors.centerIn: pane
                    width: scrolled.width
                    height: 40
                    radius: 10.0
                    border.width: 1
                    color: '#f5801f'
                    Text {
                        anchors.centerIn: parent
                        text: modelData.content
                    }
                }
            }
        }
        
        Text {
            id: message
        }
        QueryModel {
            id: model
            Component.onCompleted: {
                repeater.model = Net.toListModel(model.results)
            }
        }
    }
}
