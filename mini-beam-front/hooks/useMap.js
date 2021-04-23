import {useRef, useEffect, useState } from "react";
import {setSearch} from 'reducers/actions';
import {useDispatch, useSelector} from 'react-redux'


const useMap=()=>{
  const mapRef = useRef(null);
  let [mapInstance, setMap] = useState(null);
  const dispatch = useDispatch();
  const {lat, lng, numScooters, searchRadius} = useSelector(state=>({lat: state.lat,lng: state.lng}));
  useEffect(() => {
    let google = window.google;
    mapInstance = mapRef.current;
    const myLatlng = new google.maps.LatLng(lat, lng);
    const mapOptions = {
      zoom: 14,
      center: myLatlng,
      scrollwheel: false,
      zoomControl: true,
      mapTypeControl: true, 
      mapTypeControlOptions: {
        style: google.maps.MapTypeControlStyle.DROPDOWN_MENU,
        mapTypeIds: ["roadmap", "terrain"],
      },
    };

    mapInstance = new google.maps.Map(mapInstance, mapOptions);
    google.maps.event.addListener(mapInstance, "center_changed", function() {
      const center = this.getCenter();
      const lat = center.lat();
      const lng = center.lng();
      dispatch(setSearch({lat, lng}))
    });
    setMap(mapInstance);
  }, []);
  return {mapRef, mapInstance};
}

export default useMap;