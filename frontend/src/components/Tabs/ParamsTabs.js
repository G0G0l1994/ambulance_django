import { Grid, GridItem, Text, Input, HStack } from "@chakra-ui/react";
import { useEffect, useState } from "react";

const ParamsTabs = ({ params, onRefSave }) => {
    const [localData, setLocalData] = useState(params || {});

    // Обновляем localData при изменении пропсов
    useEffect(() => {
        if (params) {
            setLocalData(params);
        }
    }, [params]);

    const handleChange = (field, value) => {
        setLocalData((prev) => ({
            ...prev,
            [field]: value,
        }));
    };

    useEffect(() => {
        if (onRefSave) {
            onRefSave.current = () => localData || {};
        }
    }, [localData, onRefSave]);

    return (
        <Grid gap={6} templateColumns="repeat(2, 1fr)">
            <GridItem columnGap={6}>
                <HStack p={2}>
                    <Text w="150px">Температура</Text>
                    <Input
                        size="sm"
                        boxSize="50px"
                        w="70px"
                        value={localData.temperature}
                        onChange={(e) => {
                            handleChange("temperature", e.target.value);
                        }}
                    />
                </HStack>
                <HStack alignItems="center" p={2}>
                    <Text w="150px">Артериальное давление</Text>
                    <Input
                        size="sm"
                        boxSize="50px"
                        w="70px"
                        value={localData.blood_pressure_systolic}
                        onChange={(e) => {
                            handleChange(
                                "blood_pressure_systolic",
                                e.target.value
                            );
                        }}
                    />{" "}
                    <Text>/</Text>{" "}
                    <Input
                        size="sm"
                        boxSize="50px"
                        w="70px"
                        value={localData.blood_pressure_diastolic}
                        onChange={(e) => {
                            handleChange(
                                "blood_pressure_diastolic",
                                e.target.value
                            );
                        }}
                    />
                </HStack>
                <HStack alignItems="center" p={2}>
                    <Text w="150px">Глюкоза</Text>
                    <Input
                        size="sm"
                        boxSize="50px"
                        w="70px"
                        value={localData.blood_glucose}
                        onChange={(e) => {
                            handleChange("blood_glucose", e.target.value);
                        }}
                    />
                </HStack>
                <HStack alignItems="center" p={2}>
                    <Text w="150px">SpO2</Text>
                    <Input
                        size="sm"
                        boxSize="50px"
                        w="70px"
                        value={localData.saturation}
                        onChange={(e) => {
                            handleChange("saturation", e.target.value);
                        }}
                    />
                </HStack>
            </GridItem>
            <GridItem columnGap={6}>
                <HStack p={2}>
                    <Text w="150px">ЧСС</Text>
                    <Input
                        size="sm"
                        boxSize="50px"
                        w="70px"
                        value={localData.heartbite}
                        onChange={(e) => {
                            handleChange("heartbite", e.target.value);
                        }}
                    />
                </HStack>
                <HStack p={2}>
                    <Text w="150px">Пульс</Text>
                    <Input
                        size="sm"
                        boxSize="50px"
                        w="70px"
                        value={localData.pulse}
                        onChange={(e) => {
                            handleChange("pulse", e.target.value);
                        }}
                    />
                </HStack>
                <HStack p={2}>
                    <Text w="150px">ЧДД</Text>
                    <Input
                        size="sm"
                        boxSize="50px"
                        w="70px"
                        value={localData.respiratory_rate}
                        onChange={(e) => {
                            handleChange("respiratory_rate", e.target.value);
                        }}
                    />
                </HStack>
            </GridItem>
        </Grid>
    );
};

export default ParamsTabs;
