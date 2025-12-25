import { Textarea, Text, Input, HStack } from "@chakra-ui/react";

export const InputTextField = ({ fieldname, onChange, name }) => {
  return (
    <HStack align="center" spacing={4} w="30%">
      <Text> {fieldname}</Text>
      <Textarea onChange={onChange} name={name}></Textarea>
    </HStack>
  );
};

export const InputField = ({ fieldname, placeholder, onChange, name }) => {
  return (
    <HStack align="center" spacing={4} w="30%">
      <Text> {fieldname}</Text>
      <Input placeholder={placeholder} onChange={onChange} name={name} />
    </HStack>
  );
};

export const DateField = ({ fieldname, placeholder, name, onChange }) => {
  return (
    <HStack align="left" spacing={4} w="20%">
      <Text> {fieldname}</Text>
      <Input placeholder={placeholder} name={name} onChange={onChange} />
    </HStack>
  );
};
