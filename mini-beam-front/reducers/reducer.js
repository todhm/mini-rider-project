import {ActionTypes} from 'reducers/actions';


const mapReducer = (state = {}, action) => {
  switch (action.type) {
      case ActionTypes.SET_SEARCH:
        return {
          ...state,
          ...action.payloads,
        }
      case ActionTypes.SET_SCOOTER_LIST:
        return {
          ...state,
          scooterList: [
            ...action.payloads,
          ]
        }
      default:
          return state;
  }
};

export default mapReducer;