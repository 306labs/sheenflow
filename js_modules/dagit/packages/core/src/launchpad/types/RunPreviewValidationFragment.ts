/* tslint:disable */
/* eslint-disable */
// @generated
// This file was automatically generated and should not be edited.

import { EvaluationErrorReason } from "./../../types/globalTypes";

// ====================================================
// GraphQL fragment: RunPreviewValidationFragment
// ====================================================

export interface RunPreviewValidationFragment_PipelineConfigValidationValid {
  __typename: "PipelineConfigValidationValid";
}

export interface RunPreviewValidationFragment_RunConfigValidationInvalid_errors_RuntimeMismatchConfigError_stack_entries_EvaluationStackPathEntry {
  __typename: "EvaluationStackPathEntry";
  fieldName: string;
}

export interface RunPreviewValidationFragment_RunConfigValidationInvalid_errors_RuntimeMismatchConfigError_stack_entries_EvaluationStackListItemEntry {
  __typename: "EvaluationStackListItemEntry";
  listIndex: number;
}

export interface RunPreviewValidationFragment_RunConfigValidationInvalid_errors_RuntimeMismatchConfigError_stack_entries_EvaluationStackMapKeyEntry {
  __typename: "EvaluationStackMapKeyEntry";
  mapKey: any;
}

export interface RunPreviewValidationFragment_RunConfigValidationInvalid_errors_RuntimeMismatchConfigError_stack_entries_EvaluationStackMapValueEntry {
  __typename: "EvaluationStackMapValueEntry";
  mapKey: any;
}

export type RunPreviewValidationFragment_RunConfigValidationInvalid_errors_RuntimeMismatchConfigError_stack_entries = RunPreviewValidationFragment_RunConfigValidationInvalid_errors_RuntimeMismatchConfigError_stack_entries_EvaluationStackPathEntry | RunPreviewValidationFragment_RunConfigValidationInvalid_errors_RuntimeMismatchConfigError_stack_entries_EvaluationStackListItemEntry | RunPreviewValidationFragment_RunConfigValidationInvalid_errors_RuntimeMismatchConfigError_stack_entries_EvaluationStackMapKeyEntry | RunPreviewValidationFragment_RunConfigValidationInvalid_errors_RuntimeMismatchConfigError_stack_entries_EvaluationStackMapValueEntry;

export interface RunPreviewValidationFragment_RunConfigValidationInvalid_errors_RuntimeMismatchConfigError_stack {
  __typename: "EvaluationStack";
  entries: RunPreviewValidationFragment_RunConfigValidationInvalid_errors_RuntimeMismatchConfigError_stack_entries[];
}

export interface RunPreviewValidationFragment_RunConfigValidationInvalid_errors_RuntimeMismatchConfigError {
  __typename: "RuntimeMismatchConfigError" | "SelectorTypeConfigError";
  reason: EvaluationErrorReason;
  message: string;
  stack: RunPreviewValidationFragment_RunConfigValidationInvalid_errors_RuntimeMismatchConfigError_stack;
}

export interface RunPreviewValidationFragment_RunConfigValidationInvalid_errors_MissingFieldConfigError_stack_entries_EvaluationStackPathEntry {
  __typename: "EvaluationStackPathEntry";
  fieldName: string;
}

export interface RunPreviewValidationFragment_RunConfigValidationInvalid_errors_MissingFieldConfigError_stack_entries_EvaluationStackListItemEntry {
  __typename: "EvaluationStackListItemEntry";
  listIndex: number;
}

export interface RunPreviewValidationFragment_RunConfigValidationInvalid_errors_MissingFieldConfigError_stack_entries_EvaluationStackMapKeyEntry {
  __typename: "EvaluationStackMapKeyEntry";
  mapKey: any;
}

export interface RunPreviewValidationFragment_RunConfigValidationInvalid_errors_MissingFieldConfigError_stack_entries_EvaluationStackMapValueEntry {
  __typename: "EvaluationStackMapValueEntry";
  mapKey: any;
}

export type RunPreviewValidationFragment_RunConfigValidationInvalid_errors_MissingFieldConfigError_stack_entries = RunPreviewValidationFragment_RunConfigValidationInvalid_errors_MissingFieldConfigError_stack_entries_EvaluationStackPathEntry | RunPreviewValidationFragment_RunConfigValidationInvalid_errors_MissingFieldConfigError_stack_entries_EvaluationStackListItemEntry | RunPreviewValidationFragment_RunConfigValidationInvalid_errors_MissingFieldConfigError_stack_entries_EvaluationStackMapKeyEntry | RunPreviewValidationFragment_RunConfigValidationInvalid_errors_MissingFieldConfigError_stack_entries_EvaluationStackMapValueEntry;

export interface RunPreviewValidationFragment_RunConfigValidationInvalid_errors_MissingFieldConfigError_stack {
  __typename: "EvaluationStack";
  entries: RunPreviewValidationFragment_RunConfigValidationInvalid_errors_MissingFieldConfigError_stack_entries[];
}

export interface RunPreviewValidationFragment_RunConfigValidationInvalid_errors_MissingFieldConfigError_field {
  __typename: "ConfigTypeField";
  name: string;
}

export interface RunPreviewValidationFragment_RunConfigValidationInvalid_errors_MissingFieldConfigError {
  __typename: "MissingFieldConfigError";
  reason: EvaluationErrorReason;
  message: string;
  stack: RunPreviewValidationFragment_RunConfigValidationInvalid_errors_MissingFieldConfigError_stack;
  field: RunPreviewValidationFragment_RunConfigValidationInvalid_errors_MissingFieldConfigError_field;
}

export interface RunPreviewValidationFragment_RunConfigValidationInvalid_errors_MissingFieldsConfigError_stack_entries_EvaluationStackPathEntry {
  __typename: "EvaluationStackPathEntry";
  fieldName: string;
}

export interface RunPreviewValidationFragment_RunConfigValidationInvalid_errors_MissingFieldsConfigError_stack_entries_EvaluationStackListItemEntry {
  __typename: "EvaluationStackListItemEntry";
  listIndex: number;
}

export interface RunPreviewValidationFragment_RunConfigValidationInvalid_errors_MissingFieldsConfigError_stack_entries_EvaluationStackMapKeyEntry {
  __typename: "EvaluationStackMapKeyEntry";
  mapKey: any;
}

export interface RunPreviewValidationFragment_RunConfigValidationInvalid_errors_MissingFieldsConfigError_stack_entries_EvaluationStackMapValueEntry {
  __typename: "EvaluationStackMapValueEntry";
  mapKey: any;
}

export type RunPreviewValidationFragment_RunConfigValidationInvalid_errors_MissingFieldsConfigError_stack_entries = RunPreviewValidationFragment_RunConfigValidationInvalid_errors_MissingFieldsConfigError_stack_entries_EvaluationStackPathEntry | RunPreviewValidationFragment_RunConfigValidationInvalid_errors_MissingFieldsConfigError_stack_entries_EvaluationStackListItemEntry | RunPreviewValidationFragment_RunConfigValidationInvalid_errors_MissingFieldsConfigError_stack_entries_EvaluationStackMapKeyEntry | RunPreviewValidationFragment_RunConfigValidationInvalid_errors_MissingFieldsConfigError_stack_entries_EvaluationStackMapValueEntry;

export interface RunPreviewValidationFragment_RunConfigValidationInvalid_errors_MissingFieldsConfigError_stack {
  __typename: "EvaluationStack";
  entries: RunPreviewValidationFragment_RunConfigValidationInvalid_errors_MissingFieldsConfigError_stack_entries[];
}

export interface RunPreviewValidationFragment_RunConfigValidationInvalid_errors_MissingFieldsConfigError_fields {
  __typename: "ConfigTypeField";
  name: string;
}

export interface RunPreviewValidationFragment_RunConfigValidationInvalid_errors_MissingFieldsConfigError {
  __typename: "MissingFieldsConfigError";
  reason: EvaluationErrorReason;
  message: string;
  stack: RunPreviewValidationFragment_RunConfigValidationInvalid_errors_MissingFieldsConfigError_stack;
  fields: RunPreviewValidationFragment_RunConfigValidationInvalid_errors_MissingFieldsConfigError_fields[];
}

export interface RunPreviewValidationFragment_RunConfigValidationInvalid_errors_FieldNotDefinedConfigError_stack_entries_EvaluationStackPathEntry {
  __typename: "EvaluationStackPathEntry";
  fieldName: string;
}

export interface RunPreviewValidationFragment_RunConfigValidationInvalid_errors_FieldNotDefinedConfigError_stack_entries_EvaluationStackListItemEntry {
  __typename: "EvaluationStackListItemEntry";
  listIndex: number;
}

export interface RunPreviewValidationFragment_RunConfigValidationInvalid_errors_FieldNotDefinedConfigError_stack_entries_EvaluationStackMapKeyEntry {
  __typename: "EvaluationStackMapKeyEntry";
  mapKey: any;
}

export interface RunPreviewValidationFragment_RunConfigValidationInvalid_errors_FieldNotDefinedConfigError_stack_entries_EvaluationStackMapValueEntry {
  __typename: "EvaluationStackMapValueEntry";
  mapKey: any;
}

export type RunPreviewValidationFragment_RunConfigValidationInvalid_errors_FieldNotDefinedConfigError_stack_entries = RunPreviewValidationFragment_RunConfigValidationInvalid_errors_FieldNotDefinedConfigError_stack_entries_EvaluationStackPathEntry | RunPreviewValidationFragment_RunConfigValidationInvalid_errors_FieldNotDefinedConfigError_stack_entries_EvaluationStackListItemEntry | RunPreviewValidationFragment_RunConfigValidationInvalid_errors_FieldNotDefinedConfigError_stack_entries_EvaluationStackMapKeyEntry | RunPreviewValidationFragment_RunConfigValidationInvalid_errors_FieldNotDefinedConfigError_stack_entries_EvaluationStackMapValueEntry;

export interface RunPreviewValidationFragment_RunConfigValidationInvalid_errors_FieldNotDefinedConfigError_stack {
  __typename: "EvaluationStack";
  entries: RunPreviewValidationFragment_RunConfigValidationInvalid_errors_FieldNotDefinedConfigError_stack_entries[];
}

export interface RunPreviewValidationFragment_RunConfigValidationInvalid_errors_FieldNotDefinedConfigError {
  __typename: "FieldNotDefinedConfigError";
  reason: EvaluationErrorReason;
  message: string;
  stack: RunPreviewValidationFragment_RunConfigValidationInvalid_errors_FieldNotDefinedConfigError_stack;
  fieldName: string;
}

export interface RunPreviewValidationFragment_RunConfigValidationInvalid_errors_FieldsNotDefinedConfigError_stack_entries_EvaluationStackPathEntry {
  __typename: "EvaluationStackPathEntry";
  fieldName: string;
}

export interface RunPreviewValidationFragment_RunConfigValidationInvalid_errors_FieldsNotDefinedConfigError_stack_entries_EvaluationStackListItemEntry {
  __typename: "EvaluationStackListItemEntry";
  listIndex: number;
}

export interface RunPreviewValidationFragment_RunConfigValidationInvalid_errors_FieldsNotDefinedConfigError_stack_entries_EvaluationStackMapKeyEntry {
  __typename: "EvaluationStackMapKeyEntry";
  mapKey: any;
}

export interface RunPreviewValidationFragment_RunConfigValidationInvalid_errors_FieldsNotDefinedConfigError_stack_entries_EvaluationStackMapValueEntry {
  __typename: "EvaluationStackMapValueEntry";
  mapKey: any;
}

export type RunPreviewValidationFragment_RunConfigValidationInvalid_errors_FieldsNotDefinedConfigError_stack_entries = RunPreviewValidationFragment_RunConfigValidationInvalid_errors_FieldsNotDefinedConfigError_stack_entries_EvaluationStackPathEntry | RunPreviewValidationFragment_RunConfigValidationInvalid_errors_FieldsNotDefinedConfigError_stack_entries_EvaluationStackListItemEntry | RunPreviewValidationFragment_RunConfigValidationInvalid_errors_FieldsNotDefinedConfigError_stack_entries_EvaluationStackMapKeyEntry | RunPreviewValidationFragment_RunConfigValidationInvalid_errors_FieldsNotDefinedConfigError_stack_entries_EvaluationStackMapValueEntry;

export interface RunPreviewValidationFragment_RunConfigValidationInvalid_errors_FieldsNotDefinedConfigError_stack {
  __typename: "EvaluationStack";
  entries: RunPreviewValidationFragment_RunConfigValidationInvalid_errors_FieldsNotDefinedConfigError_stack_entries[];
}

export interface RunPreviewValidationFragment_RunConfigValidationInvalid_errors_FieldsNotDefinedConfigError {
  __typename: "FieldsNotDefinedConfigError";
  reason: EvaluationErrorReason;
  message: string;
  stack: RunPreviewValidationFragment_RunConfigValidationInvalid_errors_FieldsNotDefinedConfigError_stack;
  fieldNames: string[];
}

export type RunPreviewValidationFragment_RunConfigValidationInvalid_errors = RunPreviewValidationFragment_RunConfigValidationInvalid_errors_RuntimeMismatchConfigError | RunPreviewValidationFragment_RunConfigValidationInvalid_errors_MissingFieldConfigError | RunPreviewValidationFragment_RunConfigValidationInvalid_errors_MissingFieldsConfigError | RunPreviewValidationFragment_RunConfigValidationInvalid_errors_FieldNotDefinedConfigError | RunPreviewValidationFragment_RunConfigValidationInvalid_errors_FieldsNotDefinedConfigError;

export interface RunPreviewValidationFragment_RunConfigValidationInvalid {
  __typename: "RunConfigValidationInvalid";
  errors: RunPreviewValidationFragment_RunConfigValidationInvalid_errors[];
}

export interface RunPreviewValidationFragment_PipelineNotFoundError {
  __typename: "PipelineNotFoundError";
  message: string;
}

export interface RunPreviewValidationFragment_InvalidSubsetError {
  __typename: "InvalidSubsetError";
  message: string;
}

export interface RunPreviewValidationFragment_PythonError_errorChain_error {
  __typename: "PythonError";
  message: string;
  stack: string[];
}

export interface RunPreviewValidationFragment_PythonError_errorChain {
  __typename: "ErrorChainLink";
  isExplicitLink: boolean;
  error: RunPreviewValidationFragment_PythonError_errorChain_error;
}

export interface RunPreviewValidationFragment_PythonError {
  __typename: "PythonError";
  message: string;
  stack: string[];
  errorChain: RunPreviewValidationFragment_PythonError_errorChain[];
}

export type RunPreviewValidationFragment = RunPreviewValidationFragment_PipelineConfigValidationValid | RunPreviewValidationFragment_RunConfigValidationInvalid | RunPreviewValidationFragment_PipelineNotFoundError | RunPreviewValidationFragment_InvalidSubsetError | RunPreviewValidationFragment_PythonError;