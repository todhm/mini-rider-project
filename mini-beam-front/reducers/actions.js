import {getParamsData} from 'api/utils';

const BaseConstants = {
  'SET_SEARCH': 'SET_SEARCH',
  'SET_SCOOTER_LIST': 'SET_SCOOTER_LIST'
};


export const setSearch=(payloads)=>{
  return {
    type: ActionTypes.SET_SEARCH,
    payloads
  };
}

export const makeSearch=(payloads)=>{
  return (dispatch)=>{
    getParamsData('/scooters', payloads).then((res)=>{
      dispatch({
        type: ActionTypes.SET_SCOOTER_LIST,
        payloads: res.data,
        })
    }).catch((e) => {
        console.error("Network Failures");
        console.error(e);
    });
  }
}

export const ActionTypes = Object.assign({}, BaseConstants);

