import { Select, HStack, Text } from "@chakra-ui/react";

export const SelectChoice = ({
  options = [],
  fieldname,
  defaultValue,
  onChange,
}) => {
  return (
    <HStack spacing={4} p={2}>
      {fieldname && <Text minW="100px">{fieldname}</Text>}
      <Select value={defaultValue} onChange={onChange}>
        {options.map(({ value: value, name }, index) => {
          return (
            <option key={index} value={value}>
              {name}
            </option>
          );
        })}
      </Select>
    </HStack>
  );
};
