import { createStore, applyMiddleware } from "redux";
import ReduxThunk from "redux-thunk";
import mapReducer from 'reducers/reducer';


const configureStore=(initialState = {
  lat : "1.358817",
  lng : "103.872186",
  searchRadius: 1000,
  numScooters: 20,
  scooterList: [],
}) => {
  
  const store = createStore(
    mapReducer,
    initialState,
    applyMiddleware(ReduxThunk)
  );


  return store;
};

export default configureStore