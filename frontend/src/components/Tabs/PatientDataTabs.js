import { useEffect, useState } from "react";
import { HStack, Input, Text, VStack, Grid, GridItem } from "@chakra-ui/react";

const PatientTab = ({ patient, onSaveRef, address }) => {
    const [localData, setLocalData] = useState(patient);
    const [localAddress, setLocalAddress] = useState(address);

    useEffect(() => {
        setLocalAddress(address);
    }, [address]);

    useEffect(() => {
        setLocalData(patient);
    }, [patient]);

    const handleChange = (field, value) => {
        setLocalData((prev) => ({ ...prev, [field]: value }));
    };
    const handleAddressChange = (value) => {
        setLocalAddress(value);
    };

    // ⬇️ даём родителю способ забрать актуальные данные
    useEffect(() => {
        if (onSaveRef) {
            onSaveRef.current = () => {
                // Возвращаем данные пациента и адрес
                // Адрес передаем через специальное поле _address, так как он не в модели Patient
                return {
                    ...(localData || {}),
                    _address: localAddress,
                };
            };
        }
    }, [localData, localAddress, onSaveRef]);

    return (
        <Grid gap={5} templateColumns="repeat(2, 1fr)">
            <GridItem columnGap={1}>
                <HStack>
                    <Text>Имя:</Text>
                    <Input
                        value={localData.first_name || ""}
                        onChange={(e) =>
                            handleChange("first_name", e.target.value)
                        }
                    />
                </HStack>
                <HStack>
                    <Text>Фамилия:</Text>
                    <Input
                        value={localData.last_name || ""}
                        onChange={(e) =>
                            handleChange("last_name", e.target.value)
                        }
                    />
                </HStack>
                <HStack>
                    <Text>Отчество:</Text>
                    <Input
                        value={localData.surname || ""}
                        onChange={(e) =>
                            handleChange("surname", e.target.value)
                        }
                    />
                </HStack>
            </GridItem>
            <GridItem>
                <HStack>
                    <Text>Дата рождения:</Text>
                    <Input
                        value={new Date(
                            localData.date_of_birth || " "
                        ).toLocaleDateString("ru-ru")}
                        onChange={(e) =>
                            handleChange("date_of_birth", e.target.value)
                        }
                    />
                </HStack>
                <HStack>
                    <Text>Адрес:</Text>
                    <Input
                        value={localAddress || " "}
                        onChange={(e) => handleAddressChange(e.target.value)}
                    />
                </HStack>
            </GridItem>
        </Grid>
    );
};

export default PatientTab;
