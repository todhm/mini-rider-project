import getConfig from "next/config";
import { Provider } from "react-redux";
import Header from 'components/Header';
import GoogleMap from 'components/GoogleMap'
import configureStore from 'reducers/configureStore';


const IndexPage = ({apiKey}) => {
  const store = configureStore();
  return (
    <>
      <Header>
        <script src={`https://maps.googleapis.com/maps/api/js?key=${apiKey}`}></script>
      </Header>
      <Provider store={store}>
      <GoogleMap/>
      </Provider>
    </>
  );
};

IndexPage.getInitialProps = async (appContext) => {
  const { serverRuntimeConfig } = getConfig();
  return {
    apiKey: serverRuntimeConfig.GOOGLE_API_KEY,
  };
};


export default IndexPage;
