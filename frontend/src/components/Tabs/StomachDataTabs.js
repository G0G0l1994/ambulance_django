import {
  Grid,
  GridItem,
  HStack,
  Input,
  Text,
  Checkbox,
} from "@chakra-ui/react";
import { useEffect, useState } from "react";

import { SelectChoice } from "../choice.field";
import {
  PAIN_STOMACH_CHOICES,
  CHARACTERISTIC_STOMACH_CHOICES,
  FORMED_TYPE_STOOL_CHOICES,
  REGULAR_STOOL_CHOICES,
} from "../../constants/select-text";

const StomachDataTabs = ({ stomach, onRefSave }) => {
  const [localData, setLocalData] = useState(stomach);

  const handleChange = (field, value) => {
    setLocalData((prev) => ({
      ...prev,
      [field]: value,
    }));
  };

  useEffect(() => {
    if (onRefSave) {
      onRefSave.current = () => localData;
    }
  }, [localData, onRefSave]);

  return (
    <Grid templateColumns="repeat(2, 1fr)">
      <GridItem columnGap={6}>
        <SelectChoice
          fieldname="Болезненность живота"
          options={PAIN_STOMACH_CHOICES}
          defaultValue={localData.pain_stomach}
          onChange={(e) => {
            handleChange("pain_stomach", e.target.value);
          }}
        />
        <SelectChoice
          fieldname="Живот"
          options={CHARACTERISTIC_STOMACH_CHOICES}
          defaultValue={localData.characteristic_stomach}
          onChange={(e) => {
            handleChange("characteristic_stomach", e.target.value);
          }}
        />
        <SelectChoice
          fieldname="Стул"
          options={FORMED_TYPE_STOOL_CHOICES}
          defaultValue={localData.formed_type_stool}
          onChange={(e) => {
            handleChange("formed_type_stool", e.target.value);
          }}
        />
        <SelectChoice
          fieldname="Регулярность стула"
          options={REGULAR_STOOL_CHOICES}
          defaultValue={localData.regular_stool}
          onChange={(e) => {
            handleChange("regular_stool", e.target.value);
          }}
        />
        <HStack gap={6} p={2}>
          <Text gap={6}> Количество в сутки</Text>
          <Input
            value={localData.rate_stool}
            boxSize="50px"
            w="70px"
            onChange={(e) => {
              handleChange("rate_stool", e.target.value);
            }}
          />
        </HStack>
      </GridItem>
      <GridItem columnGap={6}>
        <Checkbox
          pt="10px"
          pl="10px"
          isChecked={localData.involved_in_the_act_of_breathing}
          onChange={(e) => {
            handleChange("involved_in_the_act_of_breathing", e.target.checked);
          }}
        >
          Участвует в акте дыхания
        </Checkbox>
        <Text p="10px">Симптомы:</Text>
        <Checkbox
          pl="10px"
          isChecked={localData.is_shchetkin_blumberg}
          onChange={(e) => {
            handleChange("is_shchetkin_blumberg", e.target.checked);
          }}
        >
          Щеткина-Блюмберга
        </Checkbox>
        <Checkbox
          pl="10px"
          isChecked={localData.is_voskresensky}
          onChange={(e) => {
            handleChange("is_voskresensky", e.target.checked);
          }}
        >
          Воскресенского
        </Checkbox>
        <Checkbox
          pl="10px"
          pt="10px"
          isChecked={localData.is_ortner}
          onChange={(e) => {
            handleChange("is_ortner", e.target.checked);
          }}
        >
          Ортнера
        </Checkbox>
        <Checkbox
          pl="10px"
          pt="10px"
          isChecked={localData.is_rovzinga}
          onChange={(e) => {
            handleChange("is_rovzinga", e.target.checked);
          }}
        >
          Ровзинга
        </Checkbox>
        <Checkbox
          pl="10px"
          pt="10px"
          isChecked={localData.is_sitkovsky}
          onChange={(e) => {
            handleChange("is_sitkovsky", e.target.checked);
          }}
        >
          Ситковского
        </Checkbox>
        <Checkbox
          pl="10px"
          pt="10px"
          isChecked={localData.is_obraztsova}
          onChange={(e) => {
            handleChange("is_obraztsova", e.target.checked);
          }}
        >
          Образцова
        </Checkbox>
        <Checkbox
          pl="10px"
          pt="10px"
          isChecked={localData.is_murphy}
          onChange={(e) => {
            handleChange("is_murphy", e.target.checked);
          }}
        >
          Мерфи
        </Checkbox>
      </GridItem>
    </Grid>
  );
};

export default StomachDataTabs;
