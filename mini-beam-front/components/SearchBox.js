import React from 'react';
import {useSelector, useDispatch} from 'react-redux'
import {setSearch, makeSearch} from 'reducers/actions';
import Grid from '@material-ui/core/Grid';
import makeStyles from '@material-ui/core/styles/makeStyles';
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import PropTypes from "prop-types";
import useMarkers from 'hooks/useMarkers';


const useStyles = makeStyles({
  grid: {
    position: props=>props.position,
    zIndex: 2,
  },
  searchBox: {
    backgroundColor: "white",

  },
  root: {
    marginBottom: 10,
    width: "100%",
  },
  buttonRoot: {
    width: "100%",
    backgroundColor: "#0063cc",
  }
});


const SearchBox = ({mapInstance, isPc})=>{
  const flexPosition = isPc? "flex-end": "center";
  const styleProps = {position: isPc?"fixed": "relative"};
  const {
    lat, 
    lng,
    searchRadius,
    numScooters,
  } = useSelector(state=>state);
  useMarkers(mapInstance);
  const classes = useStyles(styleProps);
  const dispatch = useDispatch();
  

  return (
    <Grid container className={classes.grid} justify={flexPosition}>
      <Grid className={classes.searchBox} item sm={3} xs ={12}>
        <Grid container>
          <Grid item xs={6}>
              <TextField
                className={classes.root}
                label="Latitude"
                type="number"
                value={lat}
                onChange={
                  (e)=>dispatch(setSearch({lat: event.target.value}))
                }
              />
          </Grid>
          <Grid item xs={6}>
            <TextField
              className={classes.root}
              label="Longitude"
              type="number"
              value={lng}
              onChange={
                (e)=>dispatch(setSearch({lng: event.target.value}))
              }
            />
          </Grid>
        </Grid>
        <Grid container>
            <TextField
              className={classes.root}
              label="Initial Search Meter"
              type="number"
              value={searchRadius}
              onChange={
                (e)=>dispatch(setSearch({searchRadius: event.target.value}))              
              }
            />
        </Grid>
        <Grid container>
            <TextField
              className={classes.root}
              label="Number of closest N scooters"
              type="number"
              value={numScooters}
              onChange={
                (e)=>dispatch(setSearch({numScooters: event.target.value}))              
              }
              
            />
        </Grid>
        <Grid container>
          <Button 
            onClick={(e)=> dispatch(makeSearch(
              {
                lat,
                lng,
                searchRadius,
                numScooters,
              }))
            }
            variant="contained" 
            color="primary" 
            className={`${classes.root} ${classes.buttonRoot}`}
          >
            Search
          </Button>
        </Grid>
      </Grid>
    </Grid>
  )
}


SearchBox.propTypes = {
  map: PropTypes.object,
  isPc: PropTypes.bool,
}
export default SearchBox;