import { useState, useEffect } from "react";
import {
  HStack,
  Input,
  Text,
  Grid,
  GridItem,
  Textarea,
  Checkbox,
} from "@chakra-ui/react";
import { SelectChoice } from "../fields/choice.field";
import {
  RHYTHMIC_CHOICES,
  TONE_OF_HEART_CHOICES,
  CHARACTERISTIC_PULSE_CHOICES,
  MURMUR_CHOICES,
} from "../../constants/select-text";

const HeartDataTabs = ({ heart, onRefSave }) => {
  const [localData, setLocalData] = useState(heart);

  const handleChange = (field, value) => {
    setLocalData((prev) => ({ ...prev, [field]: value }));
  };

  useEffect(() => {
    if (onRefSave) {
      onRefSave.current = () => localData;
    }
  }, [localData, onRefSave]);

  return (
    <Grid gap={6} templateColumns="repeat(2, 1fr)">
      <GridItem columnGap={6}>
        <SelectChoice
          fieldname="Тоны сердца"
          options={TONE_OF_HEART_CHOICES}
          defaultValue={localData.tone_of_heart}
          onChange={(e) => {
            handleChange("tone_of_heart", e.target.value);
          }}
        />
        <SelectChoice
          fieldname="Ритмичность тонов"
          options={RHYTHMIC_CHOICES}
          defaultValue={localData.rhythmic_tone}
          onChange={(e) => {
            handleChange("rhythmic_tone", e.target.value);
          }}
        />
        <SelectChoice
          fieldname="Ритмичность пульса"
          options={RHYTHMIC_CHOICES}
          defaultValue={localData.rhythmic_pulse}
          onChange={(e) => {
            handleChange("rhythmic_pulse", e.target.value);
          }}
        />
        <SelectChoice
          fieldname="Характеристика пульса"
          options={CHARACTERISTIC_PULSE_CHOICES}
          defaultValue={localData.characteristic_pulse}
          onChange={(e) => {
            handleChange("characteristic_pulse", e.target.value);
          }}
        />
      </GridItem>
      <GridItem>
        <HStack p={2}>
          <Text>Акцент тона</Text>
          <Input
            value={localData.heart_tone_accent}
            onChange={(e) => {
              handleChange("heart_tone_accent", e.target.value);
            }}
          />
        </HStack>
        <SelectChoice
          fieldname="Шумы сердца"
          options={MURMUR_CHOICES}
          defaultValue={localData.murmur}
          onChange={(e) => {
            handleChange("murmur", e.target.value);
          }}
        />
        <Checkbox
          isChecked={localData.heart_rate_deficit}
          onChange={(e) => {
            handleChange("heart_rate_deficit", e.target.checked);
          }}
        >
          {" "}
          Дефицит пульса
        </Checkbox>
      </GridItem>
    </Grid>
  );
};

export default HeartDataTabs;
