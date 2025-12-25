import { useState, useEffect } from "react";
import {
    HStack,
    Input,
    Text,
    Grid,
    GridItem,
    Textarea,
    Select,
} from "@chakra-ui/react";
import {
    GENERAL_ASSESSMENT_CHOICES,
    CONSCIOUSNESS_CHOICES,
    BODY_POSITION_CHOICES,
} from "../../constants/select-text";

const CommonDataTab = ({ common_data, onRefSave }) => {
    const [localData, setLocalData] = useState(common_data || {});

    // Обновляем localData при изменении пропсов
    useEffect(() => {
        if (common_data) {
            setLocalData(common_data);
        }
    }, [common_data]);

    const handleChange = (field, value) => {
        setLocalData((prev) => ({ ...prev, [field]: value }));
    };

    useEffect(() => {
        if (onRefSave) {
            onRefSave.current = () => localData || {};
        }
    }, [localData, onRefSave]);

    return (
        <Grid gap={5} templateColumns="repeat(1, 1fr)">
            <GridItem columnGap={3}>
                <HStack p={2}>
                    <Text>Жалобы:</Text>
                    <Textarea
                        value={localData.complaints}
                        onChange={(e) => {
                            handleChange("complaints", e.target.value);
                        }}
                    />
                </HStack>
            </GridItem>
            <GridItem>
                <HStack p={2}>
                    <Text>Анамнез:</Text>
                    <Textarea
                        value={localData.anamnesis}
                        onChange={(e) => {
                            handleChange("anamnesis", e.target.value);
                        }}
                    />
                </HStack>
            </GridItem>
            <GridItem columnGap={3}>
                <HStack p={2}>
                    <Text>Локальный статус:</Text>
                    <Textarea
                        value={localData.status_localis}
                        onChange={(e) => {
                            handleChange("status_localis", e.target.value);
                        }}
                    />
                </HStack>
            </GridItem>
            <GridItem>
                <HStack p={2}>
                    <Text>Состояние:</Text>
                    <Select
                        value={localData.general_assessment}
                        onChange={(e) => {
                            handleChange("general_assessment", e.target.value);
                        }}
                    >
                        {GENERAL_ASSESSMENT_CHOICES.map(
                            ({ value: value, name }, index) => (
                                <option value={value} key={index}>
                                    {name}
                                </option>
                            )
                        )}
                    </Select>
                </HStack>
                <HStack p={2}>
                    <Text>Сознание:</Text>
                    <Select
                        value={localData.сonsciousness}
                        onChange={(e) => {
                            handleChange("сonsciousness", e.target.value);
                        }}
                    >
                        {CONSCIOUSNESS_CHOICES.map(
                            ({ value: value, name }, index) => (
                                <option value={value} key={index}>
                                    {name}
                                </option>
                            )
                        )}
                    </Select>
                </HStack>
                <HStack p={2}>
                    <Text>Положение тела:</Text>
                    <Select
                        value={localData.body_position}
                        onChange={(e) => {
                            handleChange("body_position", e.target.value);
                        }}
                    >
                        {BODY_POSITION_CHOICES.map(
                            ({ value: value, name }, index) => (
                                <option value={value} key={index}>
                                    {name}
                                </option>
                            )
                        )}
                    </Select>
                </HStack>
                <HStack p={2}>
                    <Text>
                        {""}
                        Шкала Глазго:{" "}
                        <Input
                            size="sm"
                            boxSize="50px"
                            value={localData.glasgow_scale}
                            onChange={(e) => {
                                handleChange("glasgow_scale", e.target.value);
                            }}
                        />
                        {""}
                    </Text>
                </HStack>
                <HStack p={2}>
                    <Text align="start">
                        Привычное АД:
                        <Input
                            size="sm"
                            boxSize="50px"
                            value={localData.normal_blood_pressure_systolic}
                            onChange={(e) => {
                                handleChange(
                                    "normal_blood_pressure_systolic",
                                    e.target.value
                                );
                            }}
                        />
                        /
                        <Input
                            size="sm"
                            boxSize="50px"
                            value={localData.normal_blood_pressure_diastolic}
                            onChange={(e) => {
                                handleChange(
                                    "normal_blood_pressure_diastolic",
                                    e.target.value
                                );
                            }}
                        />
                    </Text>
                </HStack>
            </GridItem>
        </Grid>
    );
};

export default CommonDataTab;
