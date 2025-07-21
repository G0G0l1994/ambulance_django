import { Select, HStack, Text } from "@chakra-ui/react";

export const SelectChoice = ({ options = [], fieldname, name, onChange, placeholder }) => {
    return (
        <HStack spacing={4}>
            {fieldname && <Text minW="100px">{fieldname}</Text>}
            <Select name={name} onChange={onChange} placeholder={placeholder}>
                {options.map((crew) => {
                    return (
                        <option key={crew.value} value={crew.value}>
                            {crew.label}
                        </option>
                    );
                })}
            </Select>
        </HStack>
    );
};
