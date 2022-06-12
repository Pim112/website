import {Button, StyleSheet, Text, TextInput, View} from 'react-native';
import {useCallback, useEffect, useState} from "react";
import axios from "axios";
import {JWT, User, UserLoginAPI} from "./models";
import {defaultFetch, FetchMethod} from "./utils/fetch";
import {Card, Input} from "react-native-elements";

interface DataState {
  jwt?: JWT;
  user?: User,
}

export default function App() {
  const [state, setState] = useState<DataState>();
  const [email, setEmail] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [changeUsernameValue, setChangeUsernameValue] = useState<string>("");
  
  useEffect(() => {
    getUser(1)
      .then();
  }, []);
  
  const getUser = useCallback(async (id: number) => {
    const response = await defaultFetch("/userById",
      FetchMethod.GET,
      undefined,
      {id: id}
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
  
  const changeUsername = useCallback(async () => {
    const response = await defaultFetch("/user/nameChange",
      FetchMethod.PUT,
      state?.jwt,
      {username: changeUsernameValue}
    );
    
    if (response.status !== 200) {
      console.log(response);
      return;
    }
    
    setState((oldState) => ({
      ...oldState,
      user: response.data,
    }))
  }, [changeUsernameValue, state?.jwt]);
  
  const loginUser = useCallback(async () => {
    console.log(email, password);
    const user: UserLoginAPI = {email: email, password: password};
    const response = await defaultFetch("/login",
      FetchMethod.POST,
      undefined,
      JSON.stringify(user)
    );
    
    if (response.status !== 200) {
      console.log(response);
      return;
    }
    
    const jwt: JWT = response.data;
    // Fetch user data
    const userResponse = await defaultFetch("/user", FetchMethod.GET, jwt);
    let userData: User | undefined = userResponse.data;
    
    if (userResponse.status !== 200) {
      console.log(
        `UserProvider.login GET /user error: ${userResponse.status}`
      );
      userData = undefined;
    }
    
    setState({
      jwt,
      user: userData
    });
  }, [email, password])
  
  const [text, setText] = useState<string>("")
  
  return (
    <View style={styles.container}>
      <Card containerStyle={{borderRadius: 20}}>
        <Text>
          Username: {state?.user?.username}
        </Text>
        <Input textContentType="emailAddress"
               autoCompleteType="emailAddress"
               onChangeText={setEmail}
               defaultValue={email}
               style={{}}
               placeholder={"input email"}
        />
        <Input textContentType="password"
               autoCompleteType="password"
               onChangeText={setPassword}
               defaultValue={password}
               style={{}}
               placeholder={"input password"}
               secureTextEntry
        />
        <Button color="orange" title="Login" onPress={loginUser}/>
        
        <Input textContentType="username"
               autoCompleteType="username"
               onChangeText={setChangeUsernameValue}
               defaultValue={changeUsernameValue}
               style={{}}
               placeholder={"change username"}
        />
        <Button color="orange" title="Login" onPress={changeUsername}/>
      </Card>
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
  InputStyle: {
    borderWidth: 1
  },
});
