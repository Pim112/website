import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import {useEffect, useState} from "react";
import axios from "axios";

export default function App() {
  const [getRequest, setGetRequest] = useState<string>("");

  useEffect(() => {
    axios.get("http://127.0.0.1:5000")
      .then(function (response) {
        setGetRequest(response.data);
      })
      .then(function (error) {
        console.log(error);
      })
  }, []);

  return (
    <View style={styles.container}>
      {getRequest}
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
