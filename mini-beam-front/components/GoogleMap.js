import React from 'react';
import useTheme from '@material-ui/core/styles/useTheme';
import useMediaQuery from '@material-ui/core/useMediaQuery';
import useMap from 'hooks/useMap'
import SearchBox from './SearchBox';



const  GoogleMap=()=>{

  const {mapRef, mapInstance} = useMap();
  const theme = useTheme();
  const isPc = useMediaQuery(theme.breakpoints.up('sm'));

  return (
    <>
      <SearchBox mapInstance={mapInstance} isPc={isPc}/>
      <div ref={mapRef} style={{height: isPc? "100vh": "70vh"}}/>
    </>
  )
}


export default GoogleMap;