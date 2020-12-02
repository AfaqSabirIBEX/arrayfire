function(generate_product_version outfile)
  set(options)
  set(oneValueArgs
    COMPANY_NAME
    FILE_DESCRIPTION
    FILE_NAME
    ORIGINAL_FILE_NAME
    COMPANY_COPYRIGHT
  )
  set(multiValueArgs)
  cmake_parse_arguments(PRODUCT "${options}" "${oneValueArgs}" "${multiValueArgs}" ${ARGN})

  if(NOT PRODUCT_COMPANY_NAME OR "${PRODUCT_COMPANY_NAME}" STREQUAL "")
      set(PRODUCT_COMPANY_NAME "ArrayFire")
  endif()
  if(NOT PRODUCT_FILE_DESCRIPTION OR "${PRODUCT_FILE_DESCRIPTION}" STREQUAL "")
    set(PRODUCT_FILE_DESCRIPTION "ArrayFire Library")
  endif()
  if(NOT PRODUCT_FILE_NAME OR "${PRODUCT_FILE_NAME}" STREQUAL "")
    set(PRODUCT_FILE_NAME "${PROJECT_NAME}")
  endif()
  if(NOT PRODUCT_ORIGINAL_FILE_NAME OR "${PRODUCT_ORIGINAL_FILE_NAME}" STREQUAL "")
    set(PRODUCT_ORIGINAL_FILE_NAME "${PRODUCT_FILE_NAME}")
  endif()
  if(NOT PRODUCT_FILE_DESCRIPTION OR "${PRODUCT_FILE_DESCRIPTION}" STREQUAL "")
      set(PRODUCT_FILE_DESCRIPTION "${PRODUCT_FILE_NAME}")
  endif()
  if(NOT PRODUCT_COMPANY_COPYRIGHT OR "${PRODUCT_COMPANY_COPYRIGHT}" STREQUAL "")
    string(TIMESTAMP PRODUCT_CURRENT_YEAR "%Y")
    set(PRODUCT_COMPANY_COPYRIGHT "${PRODUCT_COMPANY_NAME} (C) Copyright ${PRODUCT_CURRENT_YEAR}")
  endif()

  set(PRODUCT_VERSION ${PROJECT_VERSION})
  set(PRODUCT_VERSION_MAJOR ${PROJECT_VERSION_MAJOR})
  set(PRODUCT_VERSION_MINOR ${PROJECT_VERSION_MINOR})
  set(PRODUCT_VERSION_PATCH ${PROJECT_VERSION_PATCH})
  set(PRODUCT_INTERNAL_FILE_NAME ${PRODUCT_ORIGINAL_FILE_NAME})

  set(ver_res_file "${PROJECT_BINARY_DIR}/${PRODUCT_FILE_NAME}_version_info.rc")
  configure_file(
    ${PROJECT_SOURCE_DIR}/CMakeModules/version_info.rc.in
    ${ver_res_file}
  )
  set(${outfile} ${ver_res_file} PARENT_SCOPE)
endfunction()