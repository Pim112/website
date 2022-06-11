import {StyleSheet, Text, View} from 'react-native';
import {useCallback, useEffect, useState} from "react";
import axios from "axios";
import {User, UserByIdAPI} from "./models";
import {defaultFetch, FetchMethod} from "./utils/fetch";

interface DataState {
  user?: User,
}

export default function App() {
  const [state, setState] = useState<DataState>({
    user: undefined,
  });

  useEffect(() => {
    const userById: UserByIdAPI = {id: 1};
    getUser(userById);
  }, []);

  const getUser = useCallback( async (user: UserByIdAPI) => {


    console.log(JSON.stringify(user))
    const response = await defaultFetch("/userById",
      FetchMethod.POST,
      undefined,
      JSON.stringify(user)
    );

    if (response.status !== 200) {
      console.log(response);
      return;
    }

    setState((oldState) => ({
      ...oldState,
      user: response.data,
    }))
  }, []);

  return (
    <View style={styles.container}>
      <Text>
        {state.user?.username}
      </Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
