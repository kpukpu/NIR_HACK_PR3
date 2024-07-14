import React, { useEffect } from "react";

const MapComponent = () => {
    useEffect(() => {
        const initMap = () => {
            // eslint-disable-next-line
            const map = new naver.maps.Map("map", {
                // eslint-disable-next-line
                center: new naver.maps.LatLng(37.5665, 126.9780),
                zoom: 15,
                mapTypeControl: true,
            });
            // eslint-disable-next-line
            const trafficLayer = new naver.maps.TrafficLayer();
            trafficLayer.setMap(map);

            const interval = setInterval(() => {
                trafficLayer.setMap(null);
                trafficLayer.setMap(map);
            }, 300000);

            return () => clearInterval(interval);
        };

        if (window.naver) {
            initMap();
        } else {
            window.addEventListener('load', initMap);
        }
    }, []);

    return <div id="map" style={{ width: "100%", height: "500px" }} />;
};

export default MapComponent;
