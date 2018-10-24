function PyFunction(url, data, succeed, error) {
    new QWebChannel(qt.webChannelTransport, function (channel) {
        channel.objects.pyjs.channel(url, data, function (data) {
            var responce = JSON.parse(data);
            if (responce.status === 200) {
                succeed(responce.context)
            } else {
                error(responce.context)
            }
        })
    });
}
