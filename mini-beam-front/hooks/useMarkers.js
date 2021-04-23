import {useEffect, useState } from "react";
import {useSelector, useDispatch} from 'react-redux'
import {makeSearch} from 'reducers/actions';



const useMarkers=(mapInstance)=>{
  let [markers, setMarkers] = useState([]);
  const {scooterList, lat, lng, numScooters, searchRadius} = useSelector(state=>state);
  const dispatch = useDispatch();
  useEffect(()=>{
  dispatch(makeSearch({
      lat,
      lng,
      numScooters,
      searchRadius
    }));
  }, [])
  useEffect(()=>{
    markers.map(m=>m.setMap(null));
    setMarkers(scooterList.map(scooterData=>{
      const latLng = new google.maps.LatLng(scooterData.lat, scooterData.lng);
      const marker =new google.maps.Marker({
        position: latLng,
        title: scooterData.serialNo
      });
      marker.setMap(mapInstance);
      return marker;
    }));
  }, [scooterList])


  return {markers, setMarkers};
}

export default useMarkers;